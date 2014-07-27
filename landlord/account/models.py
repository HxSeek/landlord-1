#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Organization(models.Model):
    class Meta:
        permissions = (
            ('manager', u'可以管理其他组织和审核申请'),
            ('youth_league_committee', u'可以使用会议室'),
            ('StoneDock1stFloorMeetingRoomManager', u'石头坞一楼会议室管理员'),
            ('StoneDock2ndFloorMeetingRoomManager', u'石头坞二楼会议室管理员'),
        )

    user = models.OneToOneField(User)
    chinese_name = models.CharField(max_length=30, unique=True)
    org_in_charge = models.CharField(max_length=30)
    tutor = models.CharField(max_length=20)
    tutor_contact_infor = models.CharField(max_length=30)
    director = models.CharField(max_length=20)
    director_contact_infor = models.CharField(max_length=30)
    belong_to = models.CharField(max_length=10)
    is_banned = models.BooleanField(default=True)

    def __unicode__(self):
        '''  used in account.SignUpForm to display username '''
        return self.chinese_name
