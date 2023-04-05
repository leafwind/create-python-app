# -*- coding: utf-8 -*-
import datetime
import calendar


def ts2datetime(ts):
    d = datetime.datetime.utcfromtimestamp(ts)
    return d


def datetime2ts(d):
    ts = int(calendar.timegm(d.timetuple()))
    return ts


def ts2datestr(ts):
    return ts2datetime(ts).strftime("%Y%m%d")


def datestr2ts(date_str):
    d = datetime.datetime.strptime(date_str, "%Y%m%d")
    ts = datetime2ts(d)
    return ts


def datestr_add_days(date_str, n_days):
    d = datetime.datetime.strptime(date_str, "%Y%m%d")
    d_new = d + datetime.timedelta(days=n_days)
    d_new_str = d_new.strftime("%Y%m%d")
    return d_new_str
