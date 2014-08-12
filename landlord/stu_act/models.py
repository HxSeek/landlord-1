# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Q

from landlord.common.models import Room, RoomApplication
from landlord.common.mixin import DateMixin
from landlord.custom.model_field import MultiSelectField


class StuActCenterApp(RoomApplication, DateMixin):

    TIME = (
        (u'早上', u'早上'),
        (u'下午', u'下午'),
        (u'晚上', u'晚上'),
    )

    time = MultiSelectField(max_length=50, choices=TIME)
    place = models.ForeignKey(Room)
    activity = models.CharField(max_length=30)
    activity_summary = models.CharField(max_length=200)
    sponsor = models.CharField(max_length=30, blank=True, null=True)
    sponsorship = models.CharField(max_length=30, blank=True, null=True)
    sponsorship_usage = models.CharField(max_length=40, blank=True, null=True)

    def submit(self):

        self.clean_date()

        self.place.select_strategy(self)

        return self.save()
