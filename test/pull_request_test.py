import unittest
import mock
from b2tool.commands import listall


class PullRequestTest(unittest.TestCase):

    def setUp(self):
        self.response = mock.MagicMock()
        self.response.headers = {}
        self.response.status_code = 000

    def test_get_all_pull_requests(self):
        self.response.status_code = 200

        with mock.patch("requests.get", return_value=self.response):
            res = listall('test123', '123test')

        self.assertEquals(res,  1)


    def test_get_aldest_pull_request(self):
        self.fail()