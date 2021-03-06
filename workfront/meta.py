from workfront.six import with_metaclass

missing = object()


class APIVersion(object):
    """
    Receptacle for classes for a specific API version. The classes
    can be obtained from the :class:`APIVersion` instance by attribute, eg:

    .. code-block:: python

       session = Session(...)
       api = session.api
       issue = api.Issue(session, ...)

    To find the name of a class your require, consult the :ref:`modindex`
    or use the :ref:`search` in conjunction with the `API Explorer`__.

    __ https://developers.workfront.com/api-docs/api-explorer/
    """

    def __init__(self, version):
        self.version = version
        self.by_code = {}

    def register(self, type_):
        setattr(self, type_.__name__, type_)
        self.by_code[type_.code] = type_

    def override(self, type_, replacement):
        setattr(self, type_.__name__, replacement)
        self.by_code[type_.code] = replacement

    def from_data(self, session, data):
        return self.by_code[data['objCode']](session, **data)


class FieldNotLoaded(Exception):
    """Exception raised when a field is accessed but has not been loaded."""


class Field(object):
    """
    The descriptor used for mapping Workfront fields to attributes of an
    :class:`Object`.

    When a :class:`Field` is obtained from an :class:`Object`, it's value will
    be returned, or a :class:`FieldNotLoaded` exception will be raised if it
    has not yet been loaded.

    When set, a :class:`Field` will store its value in the :class:`Object`, to
    save values back to Workfront, use :meth:`Object.save`.
    """
    def __init__(self, workfront_name):
        self.workfront_name = workfront_name
        self.__doc__ = ':class:`~workfront.meta.Field` for ``{}``'.format(
            self.workfront_name
        )

    def __get__(self, instance, owner):
        if instance is None:
            return self
        result = instance.fields.get(self.workfront_name, missing)
        if result is missing:
            raise FieldNotLoaded(self.workfront_name)
        return result

    def __set__(self, instance, value):
        instance.fields[self.workfront_name] = value


class LoadingAttribute(object):

    def __init__(self, workfront_name):
        self.workfront_name = workfront_name
        self.__doc__ = ':class:`~workfront.meta.{}` for ``{}``'.format(
            self.__class__.__name__, self.workfront_name
        )

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.workfront_name not in instance.fields:
            instance.load(self.workfront_name)
        session = instance.session
        api = session.api
        return self.process(session, api, instance.fields[self.workfront_name])

    def __set__(self, instance, value):
        raise AttributeError(self.__class__.__name__ + ' cannot be set')


class Reference(LoadingAttribute):
    """
    The descriptor used for mapping Workfront references to attributes of an
    :class:`Object`.

    When a :class:`Reference` is obtained from an :class:`Object`, a referenced
    object or ``None``, if there is no referenced object in this field, will be
    returned. If the referenced object has not yet been loaded, it will be
    loaded before being returned.

    A :class:`Reference` cannot be set, you should instead set the matching
    ``_id`` :class:`Field` to the :attr:`~Object.id` of the object you wish to
    reference.
    """

    @staticmethod
    def process(session, api, data):
        return api.from_data(session, data)


class Collection(LoadingAttribute):
    """
    The descriptor used for mapping Workfront collections to attributes of an
    :class:`Object`.

    When a :class:`Collection` is obtained from an :class:`Object`, a
    :class:`tuple` of objects, which may be empty, is returned.
    If the collection has not yet been loaded, it will be
    loaded before being returned.

    A :class:`Collection` cannot be set or modified.
    """


    @staticmethod
    def process(session, api, data):
        return tuple(api.from_data(session, object_data)
                     for object_data in data)


class ModificationTrackingDict(dict):

    def __init__(self):
        self.clean()

    def clean(self, only=None):
        if only:
            for key in only:
                self.dirty_keys.discard(key)
        else:
            self.dirty_keys = set()

    def __setitem__(self, key, value):
        super(ModificationTrackingDict, self).__setitem__(key, value)
        self.dirty_keys.add(key)

    def dirty(self):
        data = {}
        for key in self.dirty_keys:
            data[key] = self[key]
        return data


class ObjectMeta(type):

    def __new__(meta, name, bases, __dict__):

        # record field names
        field_names = set()
        for key, obj in __dict__.items():
            if isinstance(obj, Field):
                field_names.add(key)

        # limit slots
        __dict__['__slots__'] = ('session', 'fields')

        # sort out docstring
        code = __dict__.get('code')
        if code:
            __dict__['__doc__'] = (
                ':class:`~workfront.meta.Object` for ``{}``'.format(code))
        elif '__doc__' not in __dict__:
            for base in bases:
                base_doc = getattr(base, '__doc__', None)
                if base_doc:
                    __dict__['__doc__'] = base_doc
                    break

        # make the class
        cls = super(ObjectMeta, meta).__new__(meta, name, bases, __dict__)
        cls.field_names = getattr(cls, 'field_names', set()) | field_names
        return cls


class Object(with_metaclass(ObjectMeta, object)):
    """
    The base class for objects reflected from the Workfront REST API.

    Objects can be instantiated and then saved in order to create new objects,
    or retrieved from Workfront using :meth:`workfront.Session.search`
    or :meth:`workfront.Session.load`.

    Wherever ``fields`` are mentioned, they may be specified as either
    Workfront-style camel case names, or the Python-style attribute names they
    are mapped to.
    """

    registry = {}

    def __init__(self, session=None, **fields):
        self.session = session
        self.fields = ModificationTrackingDict()
        for name, value in fields.items():
            if name in self.field_names:
                setattr(self, name, value)
            else:
                self.fields[name] = value
        self.fields.clean()

    def __repr__(self):
        return '<{0}: {1}>'.format(
            self.__class__.__name__,
            ', '.join('{}={!r}'.format(f, v)
                      for (f, v) in sorted(self.fields.items()))
        )

    @property
    def id(self):
        """
        The UUID of this object in Workfront.
        It will be ``None`` if this object has not yet been saved to Workfront.
        """
        return self.fields.get('ID')

    @classmethod
    def convert_name(cls, field_name):
        if isinstance(field_name, Field):
            return field_name.workfront_name
        field = getattr(cls, field_name, None)
        if field is None:
            return field_name
        else:
            return field.workfront_name

    @classmethod
    def field_spec(cls, *field_names):
        workfront_fields = []
        for field_name in field_names:
            workfront_fields.append(cls.convert_name(field_name))
        return ','.join(workfront_fields)

    def api_url(self):
        """
        The URI of this object in Workfront, suitable for passing to any of the
        :class:`~workfront.Session` methods that generate requests.

        This method cannot be used until the object has been saved to Workfront.
        """
        if not self.id:
            raise ValueError('{0} has no ID'.format(self.__class__.__name__))
        return '/{0}/{1}'.format(self.code, self.id)

    def load(self, *field_names):
        """
        Load additional fields for this object from Workfront.

        :param field_names: Either Workfront-style camel case names or the
                            Python-style attribute names they
                            are mapped to for the fields to be loaded.
        """
        fields = self.session.get(self.api_url(),
                                  dict(fields=self.field_spec(*field_names)))
        self.fields.update(fields)
        self.fields.clean(fields)

    def save(self):
        """
        If this object has not yet been saved to Workfront, create it
        using all the current fields that have been set.

        In other cases, save only the fields that have changed on this object to
        Workfront.
        """
        if self.id is None:
            data = self.session.post('/'+self.code, self.fields)
            self.fields.update(data)
        else:
            dirty = self.fields.dirty()
            if dirty:
                self.session.put(self.api_url(), dirty)
        self.fields.clean()

    def delete(self):
        """Delete this object from Workfront."""
        self.session.delete(self.api_url())
