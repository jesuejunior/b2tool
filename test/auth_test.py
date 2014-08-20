import unittest

from b2tool.commands.auth import login
import mock 


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.response = mock.MagicMock()
        self.response.headers = {}
        self.response.status_code = 000


    def test_login_ok(self):
        self.response.status_code = 200

        with mock.patch("requests.get", return_value=self.response):
            res = login('abc123', '123abc')

        self.assertEquals(res,  True)

    def test_login_wrong(self):
        self.response.status_code = 401

        with mock.patch("requests.get", return_value=self.response):
            res = login('abc123', '123abc')

        self.assertEquals(res,  False)
