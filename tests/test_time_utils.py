import datetime

from app.time_utils import ts2datetime, datetime2ts, ts2datestr, datestr2ts, datestr_add_days


class TestUtil(object):
    def test_ts2datetime(self):
        actual = ts2datetime(1493942400)
        expected = datetime.datetime(2017, 5, 5, 0, 0, 0, 0)
        assert expected == actual

    def test_datetime2ts(self):
        actual = datetime2ts(datetime.datetime(2017, 5, 5, 0, 0, 0, 0))
        expected = 1493942400
        assert expected == actual

    def test_ts2datestr(self):
        actual = ts2datestr(1493970806)
        expected = "20170505"
        assert expected == actual

    def test_datestr2ts(self):
        actual = datestr2ts("20170505")
        expected = 1493942400
        assert expected == actual

    def test_datestr_add_days(self):
        actual = datestr_add_days("20170505", -6)
        expected = "20170429"
        assert expected == actual
