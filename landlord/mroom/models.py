# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Q
from datetime import time
from django.utils.dateformat import time_format

from landlord.common.models import Room, RoomApplication
from landlord.common.mixin import DateMixin
from landlord.common.time_table import generate_time_choices
from landlord.custom.model_field import MultiSelectField



def generate_time_choices():
    """为 checkbox 标签生成时间选项

    :returns: 返回 list.
              [(time(8,0), '8点-8点30分'),
               (time(8,30), '8点30分-9点'),
                ...
               (time(22,30), '22点30分-23点'),]
    """
    def create_format(lha, rha):
        return time_format(time(lha, rha), 'H:i:s')

    choices = list()
    ptn = u'%d点-%d点30分'
    ptn_half = u'%d点30分-%d点'
    for i in xrange(8, 23):
        choices.append((create_format(i, 0), ptn % (i, i)))
        choices.append((create_format(i, 30), ptn_half % (i, i + 1)))

    return choices


class MroomApp(RoomApplication, DateMixin):

    TIME = generate_time_choices()

    time = MultiSelectField(max_length=400, choices=TIME)
    place = models.ForeignKey(Room)
    meeting_topic = models.CharField(max_length=50)
    meeting_summary = models.CharField(max_length=200)
    remarks = models.CharField(max_length=300, blank=True, null=True)

    def submit(self):

        self.clean_date()

        self.place.select_strategy(self)

        return self.save()
