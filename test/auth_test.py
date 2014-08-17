import unittest
from b2tool.commands.auth import login
from mock import Mock, patch


class LoginTest(unittest.TestCase):

    def test_login_ok(self):

        # self.response = mock.MagicMock()
        # self.response.headers = {}
        # self.response.status_code = 200

        #Preciso fazer o mock do request.get retornar 200/401 para o metodo commands/auth/login
        #Assim a chamada nao vai na api do BB e continua o fluxo

        with patch("requests.get") as get_mock:
            get_mock.return_value = res_mock = Mock()
            res_mock.return_value.status_code = 200

            res = login('abc123', '123abc')

        self.assertEquals(res,  True)

    def test_login_wrong(self):
        self.fail()
