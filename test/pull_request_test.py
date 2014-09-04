import unittest
import mock
from b2tool.commands import listall


class PullRequestTest(unittest.TestCase):

    def setUp(self):

        self.obj = [
            {
            u"source": {
                u"branch": {
                    u"name": u"develop"
                }
            },
            u"state": u"OPEN",
            u"created_on": u"2014-08-07T03:41:17.181902+00:00",
            u"updated_on": u"2014-08-18T21:08:13.471908+00:00",
            u"merge_commit": 'null',
            u"id": 85
            },
            {
            u'source': {
                u'branch': {
                    u'name': u'feature/new-config-vagrantfile'
                },
            },
            u"state": u"OPEN",
            u"created_on": u"2014-08-13T00:55:43.127689+00:00",
            u"updated_on": u"2014-08-18T18:31:42.329587+00:00",
            u"merge_commit": 'null',
            u"id": 86
        }
        ]

        self.response = mock.MagicMock()
        self.response.headers = {}
        self.response.status_code = 000

    def test_get_all_pull_requests(self):
        self.response.status_code = 200

        with mock.patch("requests.get", return_value=self.response):
            res = listall('test123', '123test')

        self.assertEquals(res,  1)


    def test_get_oldest_pull_request(self):
        self.fail()