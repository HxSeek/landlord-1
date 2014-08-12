# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Q
from datetime import time
from django.utils.dateformat import time_format

from landlord.common.models import Room, RoomApplication
from landlord.common.mixin import DateMixin
from landlord.custom.model_field import MultiSelectField


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
