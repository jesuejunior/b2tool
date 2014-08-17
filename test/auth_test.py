import mock
import unittest
from b2tool.commands.auth import login


class LoginTest(unittest.TestCase):

    def test_login_ok(self):

        self.response = mock.MagicMock()
        self.response.headers = {}
        self.response.status_code = 200

        with mock.patch("requests.get", return_value=self.response) as get_mock:

            res = login('abc123', '123abc')


        self.assertEquals(res,  True)

    def test_login_wrong(self):
        self.fail()
