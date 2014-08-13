# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns

from .views import ApplyRoomView, ListAppView, ModifyView, Table

from landlord.stu_act.forms import StuActCenterAppForm
from landlord.stu_act.models import StuActCenterApp

from landlord.mroom.forms import MroomAppForm
from landlord.mroom.models import MroomApp


urlpatterns = patterns(
    '',
    url(r'^apply/student_activity_center/$', ApplyRoomView.as_view(),
        {'appform': StuActCenterAppForm,
         'model': StuActCenterApp,
         'name': 'Stuapply'}, name='Stuapply'),

    url(r'^list/student_activity_center/$', ListAppView.as_view(),
        {'model': StuActCenterApp,
         'title': u'学生活动中心场地申请'}, name='Stulist'),

    url(r'^table/student_activity_center/$', Table.as_view(),
        {'model': StuActCenterApp,
         'template': 'stu_table.html',
         'name': 'stuact'}, name='Stutable'),

    url(r'^modify/student_activity_center/$', ModifyView.as_view(),
        {'appform': StuActCenterAppForm,
         'model': StuActCenterApp,
         'name': 'Stumodify'}, name='Stumodify'),

    url(r'^apply/meeting_room/$', ApplyRoomView.as_view(),
        {'appform': MroomAppForm,
         'model': MroomApp,
         'name': 'Mroomapply'}, name='Mroomapply'),

    url(r'^list/meeting_room/$', ListAppView.as_view(),
        {'model': MroomApp,
         'title': u'会议室使用申请'}, name='Mroomlist'),

    url(r'^table/meeting_room/$', Table.as_view(),
        {'model': MroomApp,
         'template': 'mroom_table.html',
         'name': 'mroom'}, name='Mroomtable'),

    url(r'^modify/meeting_room/$', ModifyView.as_view(),
        {'appform': MroomAppForm,
         'model': MroomApp,
         'name': 'Mroommodify'}, name='Mroommodify'),
)
