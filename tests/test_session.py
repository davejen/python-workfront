import ssl
from workfront.six.moves.BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from threading import Thread
from unittest import TestCase

from testfixtures import compare, ShouldRaise, ShouldWarn, LogCapture

from tests.helpers import MockHTTPError, MockOpenHelper, TestObjectHelper
from workfront import Session
from workfront.meta import FieldNotLoaded
from workfront.session import SANDBOX_TEMPLATE, WorkfrontAPIError


class SessionTests(MockOpenHelper, TestCase):

    def setUp(self):
        super(SessionTests, self).setUp()
        self.log = LogCapture()
        self.addCleanup(self.log.uninstall)

    def test_basic_request(self):
        session = Session('test')
        self.server.add(
            url='/login',
            params='method=GET',
            response='{"data": "foo"}'
        )
        compare(session.get('/login'), expected='foo')
        self.server.assert_called(times=1)
        self.log.check(
            ('workfront', 'INFO',
             "url: https://test.attask-ondemand.com/attask/api/unsupported"
             "/login "
             "params: {'method': 'GET'}"),
            ('workfront', 'DEBUG',
             'returned: {\n    "data": "foo"\n}')
        )

    def test_different_protocol_and_version(self):
        self.server.base_url = ''
        session = Session('test', protocol='http', api_version='v4.0')
        self.server.add(
            url='http://test.attask-ondemand.com/attask/api/v4.0/login',
            params='method=GET',
            response='{"data": "foo"}'
        )
        compare(session.get('/login'), expected='foo')
        self.server.assert_called(times=1)

    def test_different_url_template(self):
        self.server.base_url = ''
        session = Session('test', url_template=SANDBOX_TEMPLATE)
        self.server.add(
            url='https://test.preview.workfront.com/attask/api/unsupported/login',
            params='method=GET',
            response='{"data": "foo"}'
        )
        compare(session.get('/login'), expected='foo')
        self.server.assert_called(times=1)

    def test_http_error(self):
        # somewhat hypothetical, error is usually in the return json
        session = Session('test')
        self.server.add(
            url='/login',
            params='method=GET',
            response=MockHTTPError('{"data": "foo"}', 500),
        )
        with ShouldRaise(WorkfrontAPIError('Unknown error, check log', 500)):
            session.get('/login')
        self.server.assert_called(times=1)

    def test_api_error(self):
        session = Session('test')
        self.server.add(
            url='/',
            params='method=GET',
            response='{"error":{'
                     '"class":"java.lang.UnsupportedOperationException",'
                     '"message":"you must specify an action"}}'
        )
        with ShouldRaise(WorkfrontAPIError(
                {u'message': u'you must specify an action',
                 u'class': u'java.lang.UnsupportedOperationException'},
                200
        )):
            session.get('/')
        self.server.assert_called(times=1)

    def test_api_error_str_and_repr(self):
        error = WorkfrontAPIError('data', 503)
        compare(str(error), expected="503: 'data'")
        compare(repr(error), expected="WorkfrontAPIError('data', 503)")

    def test_other_error(self):
        session = Session('test')
        self.server.add(
            url='/',
            params='method=GET',
            response=Exception('boom!')
        )
        with ShouldRaise(Exception('boom!')):
            session.get('/')
        self.server.assert_called(times=1)

    def test_bad_json(self):
        session = Session('test')
        self.server.add(
            url='/',
            params='method=GET',
            response="{'oops': 'not json'}"
        )
        with ShouldRaise(WorkfrontAPIError(
                {'exception': 'Expecting property name enclosed in double '
                              'quotes: line 1 column 2 (char 1)',
                 'response': u"{'oops': 'not json'}"},
                200
        )):
            session.get('/')
        self.server.assert_called(times=1)

    def test_insecure_context(self):
        context = ssl._create_stdlib_context()
        session = Session('test', ssl_context=context)
        self.server.add(
            url='/login',
            params='method=GET',
            response='{"data": "foo"}',
            ssl_context=context
        )
        compare(session.get('/login'), expected='foo')
        self.server.assert_called(times=1)

    def test_login(self):
        session = Session('test')
        self.server.add(
            url='/login',
            params='method=GET&username=u&password=p',
            response='{"data": {"sessionID": "x", "userID": "uid"}}'
        )
        session.login('u', 'p')
        compare(session.session_id, 'x')
        compare(session.user_id, 'uid')
        self.server.assert_called(times=1)
        return session

    def test_logout(self):
        session = self.test_login()
        self.server.add(
            url='/logout',
            params='method=GET&sessionID=x',
            response='{"data": null}'
        )
        session.logout()
        compare(session.session_id, None)
        compare(session.user_id, None)
        self.server.assert_called(times=2)

    def test_request_with_session_id(self):
        session = self.test_login()
        self.server.add(
            url='/ISSUE',
            params='method=GET&sessionID=x',
            response='{"data": "foo"}'
        )
        compare(session.get('/ISSUE'), 'foo')
        self.server.assert_called(times=2)

    def test_get_api_key(self):
        session = Session('test')
        self.server.add(
            url='/user',
            params='method=PUT&action=getApiKey&username=u&password=p',
            response='{"data": {"result": "xyz"}}'
        )
        compare(session.get_api_key('u', 'p'), 'xyz')
        self.server.assert_called(times=1)

    def test_request_with_api_key(self):
        session = Session('test', api_key='xyz')
        self.server.add(
            url='/ISSUE',
            params='method=GET&apiKey=xyz',
            response='{"data": "foo"}'
        )
        actual = session.request('GET', '/ISSUE')
        compare(actual, expected='foo')
        self.server.assert_called(times=1)

    def test_request_with_params(self):
        session = Session('test')
        self.server.add(
            url='/endpoint',
            params='method=GET&str=svalue&unicode=uvalue&int=1&float=1.0&'
                   'dict={"key": "value"}',
            response='{"data": "foo"}'
        )
        actual = session.request('GET', '/endpoint', params={
            'str': 'svalue',
            'unicode': u'uvalue',
            'int': 1,
            'float': 1.0,
            'dict': {'key': 'value'},
        })
        compare(actual, expected='foo')
        self.server.assert_called(times=1)

    def test_request_absolute_url(self):

        session = Session('test')
        self.server.add(
            url='/some/url',
            params='method=GET',
            response='{"data": "foo"}'
        )
        actual = session.request(
            'GET',
            'https://test.attask-ondemand.com/attask/api/unsupported/some/url'
        )
        compare(actual, expected='foo')
        self.server.assert_called(times=1)

    def test_request_with_dodgy_absolute_url(self):

        session = Session('test')
        with ShouldRaise(TypeError(
            'url not for this session: '
            'https://bad.example.com/attask/api/unsupported/some/url'
        )):
            session.request(
                'GET',
                'https://bad.example.com/attask/api/unsupported/some/url'
            )

    def test_get(self):
        session = self.test_login()
        self.server.add(
            url='/ISSUE',
            params='sessionID=x&method=GET',
            response='{"data": "foo"}'
        )
        actual = session.get('/ISSUE')
        compare(actual, expected='foo')
        self.server.assert_called(times=2)

    def test_post(self):
        session = self.test_login()
        self.server.add(
            url='/ISSUE',
            params='sessionID=x&method=POST',
            response='{"data": "foo"}'
        )
        actual = session.post('/ISSUE')
        compare(actual, expected='foo')
        self.server.assert_called(times=2)

    def test_put(self):
        session = Session('test', api_key='xyz')
        self.server.add(
            url='/ISSUE',
            params='method=PUT&apiKey=xyz',
            response='{"data": "foo"}'
        )
        actual = session.put('/ISSUE')
        compare(actual, expected='foo')
        self.server.assert_called(times=1)

    def test_delete(self):
        session = Session('test', api_key='xyz')
        self.server.add(
            url='/ISSUE',
            params='method=DELETE&apiKey=xyz',
            response='{"data": "foo"}'
        )
        actual = session.delete('/ISSUE')
        compare(actual, expected='foo')
        self.server.assert_called(times=1)

    def test_warn_on_unknown_api(self):
        with ShouldWarn(UserWarning(
            'No APIVersion for silly, only basic requests possible'
        )):
            Session('test', api_version='silly')


class SessionWithObjectTests(TestObjectHelper, TestCase):

    def test_basic_search(self):
        self.server.add(
            url='/TEST/search',
            params='method=GET',
            response='{"data": [{"ID": "yyy"}]}'
        )

        results = self.session.search(self.api.TestObject)
        compare(len(results), expected=1)
        obj = results[0]
        self.assertTrue(isinstance(obj, self.api.TestObject))
        compare(obj.id, 'yyy')

    def test_search_with_filters(self):
        self.server.add(
            url='/TEST/search',
            params='method=GET&fieldOne=foo:*',
            response='{"data": [{"ID": "yyy"}]}'
        )

        results = self.session.search(self.api.TestObject, field_one='foo:*')
        compare(len(results), expected=1)
        obj = results[0]
        self.assertTrue(isinstance(obj, self.api.TestObject))
        compare(obj.id, 'yyy')

    def test_extra_fields(self):
        self.server.add(
            url='/TEST/search',
            params='method=GET&fields=fieldOne,fieldTwo',
            response='{"data": [{"ID": "yyy", "fieldOne": 1, "fieldTwo": 2}]}'
        )

        results = self.session.search(self.api.TestObject,
                                      fields=('fieldOne', 'fieldTwo'))
        compare(len(results), expected=1)
        obj = results[0]
        self.assertTrue(isinstance(obj, self.api.TestObject))
        compare(obj.id, 'yyy')
        compare(obj.field_one, 1)
        compare(obj.field_two, 2)

    def test_load_single(self):
        self.server.add(
            url='/TEST',
            params='method=GET&id=xx',
            response='{"data": {"ID": "yyy", "fieldOne": 1}}'
        )
        obj = self.session.load(self.api.TestObject, 'xx')
        self.assertTrue(isinstance(obj, self.api.TestObject))
        compare(obj.id, 'yyy')
        compare(obj.field_one, 1)
        with ShouldRaise(FieldNotLoaded('fieldTwo')):
            obj.field_two

    def test_load_multiple(self):
        self.server.add(
            url='/TEST',
            params='method=GET&id=xx,yy',
            response='{"data": [{"ID": "xx", "fieldOne": 1, "fieldTwo": 2}, '
                     '{"ID": "yy", "fieldOne": 3, "fieldTwo": 4}]}'
        )
        results = self.session.load(self.api.TestObject, ['xx', 'yy'])
        compare(len(results), expected=2)
        obj = results[0]
        self.assertTrue(isinstance(obj, self.api.TestObject))
        compare(obj.id, 'xx')
        compare(obj.field_one, 1)
        compare(obj.field_two, 2)
        obj = results[1]
        self.assertTrue(isinstance(obj, self.api.TestObject))
        compare(obj.id, 'yy')
        compare(obj.field_one, 3)
        compare(obj.field_two, 4)

    def test_load_extra_fields(self):
        self.server.add(
            url='/TEST',
            params='method=GET&id=xx&fields=fieldTwo',
            response='{"data": {"ID": "xx", "fieldOne": 1, "fieldTwo": 2}}'
        )
        results = self.session.load(self.api.TestObject, ['xx'], fields=['field_two'])
        compare(len(results), expected=1)
        obj = results[0]
        self.assertTrue(isinstance(obj, self.api.TestObject))
        compare(obj.id, 'xx')
        compare(obj.field_one, 1)
        compare(obj.field_two, 2)


class Handler(BaseHTTPRequestHandler):

    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'{"data": "foo"}')

    def log_request(self, _):
        pass


class TestServer(object):

    def start(self):
        server_address = ('', 8000)
        self.server = HTTPServer(server_address, Handler)
        self.thread = Thread(target=self.server.serve_forever, args=[0.01])
        self.thread.setDaemon(True)
        self.thread.start()

    def stop(self):
        self.server.shutdown()
        self.thread.join()
        self.server.server_close()


class FunctionalTests(TestCase):

    def setUp(self):
        server = TestServer()
        server.start()
        self.addCleanup(server.stop)

    def test_request(self):
        session = Session('test', url_template='http://127.0.0.1:8000')
        compare(session.request('GET', '/uri', {'foo': 'bar'}),
                expected='foo')
