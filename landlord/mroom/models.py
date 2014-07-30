# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Q

from landlord.common.models import Room, RoomApplication
from landlord.common.mixin import DateMixin
from landlord.custom.model_field import MultiSelectField


class MroomApp(RoomApplication, DateMixin):

    TIME = (
        (u'早上', u'早上'),
        (u'下午', u'下午'),
        (u'晚上', u'晚上'),
    )

    time = MultiSelectField(max_length=400, choices=TIME)
    place = models.ForeignKey(Room, limit_choices_to=Q(belong_to='mroom'))
    meeting_topic = models.CharField(max_length=50)
    meeting_summary = models.CharField(max_length=200)
    remarks = models.CharField(max_length=300, blank=True, null=True)

    def submit(self):

        self.clean_date()

        return self.save()
