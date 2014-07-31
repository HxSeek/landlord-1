# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import Group

from landlord.account.models import Organization
from .strategies import make_strategy_by_ident, make_strategy_choices


class Room(models.Model):
    """The meeting room entity."""
    FIELDS = (
        (u'stuact', u'学生活动中心'),
        (u'exhibit', u'校园展览'),
        (u'publicity', u'校园露天'),
        (u'mroom', u'会议室'),
    )

    STRATEGY_CHOICES = make_strategy_choices()

    name = models.CharField(max_length=32)
    managers = models.ManyToManyField(Group)
    belong_to = models.CharField(max_length=10, choices=FIELDS)
    strategy_ident = models.IntegerField(choices=STRATEGY_CHOICES)

    def __unicode__(self):
        return self.name

    def select_strategy(self, applicant):
        strategy = make_strategy_by_ident(self.strategy_ident, self)
        strategy.validate(applicant)

    def judge_perms(self, managers, user):
        groups = user.groups.all()
        managers_list = [str(manager) for manager in managers.all()]

        for group in groups:
            return bool(str(group) in managers_list)


class RoomApplication(models.Model):

    organization = models.ForeignKey(Organization)
    applicant_name = models.CharField(max_length=10)
    applicant_stu_id = models.CharField(max_length=15)
    applicant_college = models.CharField(max_length=50)
    applicant_phone_number = models.CharField(max_length=30)
    application_time = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def submit(self):
        return self.save()
