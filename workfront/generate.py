"""
This is used to generate a reflected object model for a particular version of
the Workfront API using the metadata provided for that API version.
"""
import json

import os

from os.path import expanduser

import re
from logging import getLogger
from os import mkdir, path

from workfront.script import script_setup, parser_with_standard_args

logger = getLogger(__name__)

TARGET_ROOT = path.join(path.split(__file__)[0], 'versions')

CLASS_NAME_OVERRIDE = dict(
    OPTASK='Issue'
)

HEADER = """\
# generated from {url}/metadata
from ..meta import APIVersion, Object, Field, Reference, Collection

api = APIVersion('{version}')
"""

CLASS_HEADER_TEMPLATE = """

class {class_name}(Object):
    code = '{obj_code}'
"""

CLASS_MEMBER_TEMPLATE = """\
    {python_name} = {type}('{workfront_name}')
"""

CLASS_ACTION_TEMPLATE = '''
    def {python_name}({arguments}):
        """
        {docstring}
        """
        params = {{}}
        {store_params}
        data = self.session.put(self.api_url()+'/{workfront_name}', params)
        {return_clause}
'''
CLASS_ACTION_LINE_SEPERATOR = "\n        "

CLASS_FOOTER_TEMPLATE = """\

api.register({class_name})
"""

ADD_COMMENT = '''
    def add_comment(self, text):
        """
        Add a comment to the current object containing the supplied text.

        The new :class:`Comment` instance is returned, it does not need to be
        saved.
        """

        comment = self.session.api.Note(
            self.session,
            note_text = text,
            note_obj_code = self.code,
            obj_id = self.id
        )
        comment.save()
        return comment
'''

NOTE_ADD_COMMENT = '''
    def add_comment(self, text):
        """
        Add a comment to this comment.

        The new :class:`Comment` instance is returned, it does not need to be
        saved.
        """
        comment = self.session.api.Note(
            self.session,
            note_text = text,
            note_obj_code = self.note_obj_code,
            obj_id = self.obj_id,
            parent_note_id=self.id
        )
        comment.save()
        return comment
'''

CONVERT_TO_TASK = '''
    def convert_to_task(self):
        """
        Convert this issue to a task.
        The newly converted task will be returned, it does not need to be
        saved.
        """
        data = self.session.put(
            self.api_url()+'/convertToTask',
            params=dict(
                updates=dict(
                    options=['preserveIssue',
                             'preservePrimaryContact',
                             'preserveUpdates'],
                    task=dict(name=self.name,
                              description=self.description,
                              enteredByID=self.entered_by_id,
                              )
            )))
        return self.session.api.Task(self.session, ID=data['result'])
'''

UPDATE_OBJ = '''
    @property
    def update_obj(self):
        """
        The object referenced by this update.
        """
        return self.session.api.from_data(
            self.session, dict(
                ID=self.update_obj_id,
                objCode=self.update_obj_code
            ))
'''

NAME_RE = re.compile('([a-z]|^)([A-Z]+)')


def name_subber(match):
    if match.group(1):
        start = match.group(1)+'_'
    else:
        start = ''
    return start+match.group(2).lower()


def dehump(name):
    """SomeThing -> some_thing"""
    return NAME_RE.sub(name_subber, name).lower()


def prepare_target(session):
    return path.join(TARGET_ROOT,
                     session.api_version.replace('.', '')+'.py')


def get_with_cache(session, cache, path):
    if cache:
        cache_path = os.path.join(
            cache,
            session.api_version+path.replace('/', '_')+'.json'
        )
        if os.path.exists(cache_path):
            with open(cache_path) as source:
                return json.load(source)

    result = session.get(path)

    if cache:
        with open(cache_path, 'w') as dest:
            json.dump(result, dest)

    return result


def decorated_object_types(session, cache):
    for name, object_type in sorted(
        get_with_cache(session, cache, '/metadata')['objects'].items()
    ):
        code =  object_type['objCode']
        # this works around the broken urls Workfront serve for the
        # 'unsupported' api:
        detail = get_with_cache(session, cache, '/'+code.lower()+'/metadata')
        class_name = CLASS_NAME_OVERRIDE.get(code, detail['name'])
        yield class_name, code, detail


class ClassWriter(object):

    name_overrides = {
        ('Approval', 'fields', 'url'): 'url_',
        ('Work', 'fields', 'url'): 'url_',
        ('Document', 'fields', 'createProof'): 'create_proof_flag',
    }

    method_overrides = {
        ('Issue', 'add_comment'): ADD_COMMENT,
        ('Issue', 'convert_to_task'): CONVERT_TO_TASK,
        ('Note', 'add_comment'): NOTE_ADD_COMMENT,
        ('Task', 'add_comment'): ADD_COMMENT,
        ('Update', 'update_obj'): UPDATE_OBJ,
    }

    def __init__(self, class_name, code, output):
        self.class_name = class_name
        self.code = code
        self.output = output
        self.members = {}

    def write_header(self):
        self.output.write(CLASS_HEADER_TEMPLATE.format(
            class_name=self.class_name,
            obj_code=self.code
        ))

    def write_members(self, format_, details, key):
        members = details[key]
        for workfront_name in sorted(members):
            python_name = self.name_overrides.get(
                (self.class_name, key, workfront_name),
                dehump(workfront_name)
            )

            if (self.class_name, python_name) in self.method_overrides:
                continue

            if python_name in self.members:
                logger.error(
                    '{} ({}) has duplicate member name: '
                    '{!r}, first from {!r}, current from {!r}'.format(
                        self.class_name, self.code,
                        python_name, self.members[python_name], workfront_name
                    ))
            self.members[python_name] = workfront_name
            self.output.write(format_(
                python_name=python_name,
                workfront_name=workfront_name,
                details=members[workfront_name],
            ))

    def write_simple_members(self, type_, details, key):
        def formatter(python_name, workfront_name, details):
            return CLASS_MEMBER_TEMPLATE.format(
                    type=type_,
                    python_name=python_name,
                    workfront_name=workfront_name
                )
        self.write_members(formatter, details, key)

    @staticmethod
    def format_action(python_name, workfront_name, details):

        docstring = ['The ``{}`` action.'.format(workfront_name), '']
        arguments = ['self']
        store_params = []

        for argument in details.get('arguments', ()):
            workfront_arg = argument['name']
            python_arg = dehump(workfront_arg)
            docstring.append((
                ':param {python_arg}: {workfront_arg} '
                '(type: ``{type}``)'
            ).format(
                python_arg=python_arg,
                workfront_arg=workfront_arg,
                type=argument['type'],
            ))
            arguments.append(
                '{python_arg}=None'.format(
                    python_arg=python_arg
                ))
            store_params.append((
                "if {python_arg} is not None: "
                "params['{workfront_arg}'] = {python_arg}"
            ).format(
                python_arg=python_arg,
                workfront_arg=workfront_arg,
            ))

        result_type = details.get('resultType')
        if result_type:
            docstring.append(':return: ``{result_type}``'.format(
                result_type=result_type
            ))
            return_clause = "return data['result']"
        else:
            return_clause = ''

        return CLASS_ACTION_TEMPLATE.format(
            python_name=python_name,
            workfront_name=workfront_name,
            arguments=', '.join(arguments),
            docstring=CLASS_ACTION_LINE_SEPERATOR.join(docstring),
            store_params=CLASS_ACTION_LINE_SEPERATOR.join(store_params),
            return_clause=return_clause,
        )

    def write_footer(self):
        for class_name, method_name in sorted(self.method_overrides):
            if class_name == self.class_name:
                self.output.write(self.method_overrides[
                                      class_name, method_name
                                  ])
        self.output.write(CLASS_FOOTER_TEMPLATE.format(
            class_name=self.class_name,
        ))


def generate(session, cache, output_path):
    with open(output_path, 'w') as output:

        output.write(HEADER.format(url=session.url,
                                   version=session.api_version))

        for class_name, code, details in sorted(
            decorated_object_types(session, cache)
        ):

            writer = ClassWriter(class_name, code, output)
            writer.write_header()
            if 'ID' in details['fields']:
                del details['fields']['ID']
            writer.write_simple_members('Field', details, 'fields')
            writer.write_simple_members('Reference', details, 'references')
            writer.write_simple_members('Collection', details, 'collections')
            writer.write_members(writer.format_action, details, 'actions')
            writer.write_footer()


def main():
    parser = parser_with_standard_args('generate', __doc__)
    parser.add_argument('--cache',
                        help='directory in which to cache metadata downloads',
                        type=expanduser)
    args, session = script_setup(parser)
    path = prepare_target(session)
    generate(session, args.cache, path)


if __name__ == '__main__':  # pragma: no cover
    main()
