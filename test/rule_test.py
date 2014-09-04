import unittest
import datetime
from b2tool.rules import parse_date, Pull


class RuleOldestTest(unittest.TestCase):

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

    def test_get_more_old_correct(self):

        expected = {'branch': 'develop', 'id': 85}
        result = Pull.oldest(self.obj)

        self.assertEquals(expected, result)

    def test_get_when_have_one(self):
        expected = {'branch': 'develop', 'id': 85}
        result = Pull.oldest(self.obj)

        self.assertEquals(expected, result)

    def test_get_when_empty(self):
        expected = {}
        result = Pull.oldest({})

        self.assertEquals(expected, result)


class RuleHelperTest(unittest.TestCase):

    def test_parse_date_ok(self):

        date_a = "2014-08-17T05:39:38.501662+00:00"
        result = parse_date(date_a)
        self.assertEquals(result, datetime.datetime(2014, 8, 17, 5, 39, 38))

    def test_parse_date_wrong(self):

        date_b = "2014-08-18T05:39:38.501662+00:00"
        result = parse_date(date_b)
        self.assertNotEquals(result, datetime.datetime(2014, 8, 17, 5, 39, 38))
