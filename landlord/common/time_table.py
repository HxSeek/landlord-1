# -*- coding: utf-8 -*-
'''
    the strategies for choosing the time_table
'''
import copy
from datetime import time

from django.utils.dateformat import time_format

from landlord.custom.table_util import generate_date_list
from landlord.custom.table_util import get_application_this_week


def generate_time_choices():
    '''
        (time(8,0), '8点-8点30分'),
        (time(8,30), '8点30分-9点'),
        ...
        (time(22,30), '22点30分-23点'),
    '''

    s = [8, 0, 30, u'点', u'点30分']
    TIME = []
    for i in range(30):
        x, y, z, a, b = s

        if y == 30:
            t = str(x) + a + '-' + str(x + 1) + b
        else:
            t = str(x) + a + '-' + str(x) + b

        TIME.append((time_format(time(x, y), 'H:i:s'), t))

        if y == 30:
            x += 1

        s = [x, z, y, b, a]
    return TIME


class Table(object):

    ident = None
    label = None

    def __init__(self, field):
        self.field = field

    def __unicode__(self):
        return u'%d : %s' % (self.ident, self.label)

    def create_table(self, model, PLACE):
        raise NotImplementedError


class Stuact_Table(Table):

    ident = 01
    label = 'the time_table of the stuact'

    def create_table(self, model, PLACE):
        this_week_apps = get_application_this_week(model)

        TIME = [u'早上', u'下午', u'晚上']

        table = {}
        empty_time_dict = {time: None for time in TIME}

        # made the table but not sort
        for short_name, full_name in PLACE:
            table[full_name] = \
                [copy.copy(empty_time_dict) for i in range(7)]

        for app in this_week_apps:
            for time in app.time:
                table[app.place.name][app.date.weekday()][time] = app

        # sorted by time
        for l, place in PLACE:
            for day in range(7):
                table[place][day] = \
                            [table[place][day][time] for time in TIME]

        # sorted by place
        content = [(place, table[place]) for l, place in PLACE]

        return {'date': generate_date_list(),
                'content': content}


class Mroom_Table(Table):

    ident = 02
    label = 'the time_table of the mroom'

    def create_table(self, model, PLACE):
        this_week_apps = get_application_this_week(model)

        TIME = generate_time_choices()

        table = {}
        empty_time_dict = {time: None for time, l in TIME}

        for short_name, full_name in PLACE:
            table[full_name] = \
                [copy.copy(empty_time_dict) for i in range(7)]

        for app in this_week_apps:
            for time in app.time:
                table[app.place.name][app.date.weekday()][time] = app

        # sorted by time
        for l, place in PLACE:
            for day in range(7):
                table[place][day] = \
                            [table[place][day][time] for time, l in TIME]

        # sorted by place
        content = [(place, table[place]) for l, place in PLACE]

        return {'date': generate_date_list(),
                'time_list': tuple(l for time, l in TIME),
                'content': content}


_TABLE_SET = [Stuact_Table, Mroom_Table]
_TABLE_MAP = {cls.ident: cls for cls in _TABLE_SET}


def make_table_by_ident(ident, field):
    if ident not in _TABLE_MAP:
        raise ValueError('unknown strategy with ident %r' % ident)
    table_cls = _TABLE_MAP[ident]
    return table_cls(field)


def make_table_choices():
    return tuple((cls.ident, cls.label) for cls in _TABLE_SET)
