# -*- coding: utf-8 -*-
from django.db import models

from landlord.common.models import RoomApplication
from landlord.common.mixin import DateMixin


class StuActCenterApp(RoomApplication, DateMixin):

    activity = models.CharField(max_length=30)
    activity_summary = models.CharField(max_length=200)
    sponsor = models.CharField(max_length=30, blank=True, null=True)
    sponsorship = models.CharField(max_length=30, blank=True, null=True)
    sponsorship_usage = models.CharField(max_length=40, blank=True, null=True)

    def submit(self):

        self.clean_date()

        return self.save()
