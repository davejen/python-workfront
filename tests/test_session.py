import ssl
from unittest import TestCase
from urllib2 import HTTPError

from testfixtures import Replacer, compare, ShouldRaise

from tests.helpers import MockOpen, MockHTTPError
from workfront import Session
from workfront.session import SANDBOX_TEMPLATE, WorkfrontAPIError


class SessionTests(TestCase):

    def setUp(self):
        r = Replacer()
        self.addCleanup(r.restore)
        self.server = MockOpen()
        r.replace('urllib2.urlopen', self.server)

    def test_basic_request(self):
        session = Session('test')
        self.server.add(
            url='https://test.attask-ondemand.com/attask/api/unsupported/login',
            params='method=GET',
            response='{"data": "foo"}'
        )
        compare(session.get('/login'), expected='foo')
        self.server.assert_called(times=1)

    def test_different_protocol_and_version(self):
        session = Session('test', protocol='http', api_version='v4.0')
        self.server.add(
            url='http://test.attask-ondemand.com/attask/api/v4.0/login',
            params='method=GET',
            response='{"data": "foo"}'
        )
        compare(session.get('/login'), expected='foo')
        self.server.assert_called(times=1)

    def test_different_url_template(self):
        session = Session('test', url_template=SANDBOX_TEMPLATE)
        self.server.add(
            url='https://test.attasksandbox.com/attask/api/unsupported/login',
            params='method=GET',
            response='{"data": "foo"}'
        )
        compare(session.get('/login'), expected='foo')
        self.server.assert_called(times=1)

    def test_http_error(self):
        # somewhat hypothetical, error is usually in the return json
        session = Session('test')
        self.server.add(
            url='https://test.attask-ondemand.com/attask/api/unsupported/login',
            params='method=GET',
            response=MockHTTPError('{"data": "foo"}', 500),
        )
        with ShouldRaise(WorkfrontAPIError('Unknown error, check log', 500)):
            session.get('/login')
        self.server.assert_called(times=1)

    def test_api_error(self):
        session = Session('test')
        self.server.add(
            url='https://test.attask-ondemand.com/attask/api/unsupported/',
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

    def test_other_error(self):
        session = Session('test')
        self.server.add(
            url='https://test.attask-ondemand.com/attask/api/unsupported/',
            params='method=GET',
            response=Exception('boom!')
        )
        with ShouldRaise(Exception('boom!')):
            session.get('/')
        self.server.assert_called(times=1)

    def test_bad_json(self):
        session = Session('test')
        self.server.add(
            url='https://test.attask-ondemand.com/attask/api/unsupported/',
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
        context = ssl._create_unverified_context()
        session = Session('test', ssl_context=context)
        self.server.add(
            url='https://test.attask-ondemand.com/attask/api/unsupported/login',
            params='method=GET',
            response='{"data": "foo"}',
            ssl_context=context
        )
        compare(session.get('/login'), expected='foo')
        self.server.assert_called(times=1)

    def test_login(self):
        session = Session('test')
        self.server.add(
            url='https://test.attask-ondemand.com/attask/api/unsupported/login',
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
            url='https://test.attask-ondemand.com/attask/api/unsupported/logout',
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
            url='https://test.attask-ondemand.com/attask/api/unsupported/ISSUE',
            params='method=GET&sessionID=x',
            response='{"data": "foo"}'
        )
        compare(session.get('/ISSUE'), 'foo')
        self.server.assert_called(times=2)

