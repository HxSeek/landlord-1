# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Q
from datetime import time
from django.utils.dateformat import time_format

from landlord.common.models import Room, RoomApplication
from landlord.common.mixin import DateMixin
from landlord.common.time_table import generate_time_choices
from landlord.custom.model_field import MultiSelectField


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
