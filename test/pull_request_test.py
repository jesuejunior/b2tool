import unittest
import mock

class PullRequestTest(unittest.TestCase):

    def setUp(self):
        self.response = mock.MagicMock()
        self.response.headers = {}
        self.response.status_code = 000

    def test_get_all_pull_requests(self):
        self.response.status_code = 200

        with mock.patch("requests.get", return_value=self.response):
            res = list()

        self.assertEquals(res,  True)


    def test_get_aldest_pull_request(self):
        self.fail()