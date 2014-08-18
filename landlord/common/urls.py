# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns

from .views import ApplyRoomView, ListAppView, ModifyView, Table
from .views import ManageView, Delete, Approved

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
         'title': u'学生活动中心场地申请',
         'name': 'Stumanage'}, name='Stulist'),

    url(r'^table/student_activity_center/$', Table.as_view(),
        {'model': StuActCenterApp,
         'template': 'stu_table.html',
         'name': 'stuact'}, name='Stutable'),

    url(r'^manage/student_activity_center/$', ManageView.as_view(),
        {'model': StuActCenterApp,
         'title': u'学生活动中心场地申请',
         'name1': 'Stumodify',
         'name2': 'Studeleted',
         'name3': 'Stuapproved'}, name='Stumanage'),

    url(r'^modify/student_activity_center/$', ModifyView.as_view(),
        {'appform': StuActCenterAppForm,
         'model': StuActCenterApp,
         'name': 'Stumodify'}, name='Stumodify'),

    url(r'deleted/$', Delete.as_view(),
        {'model': StuActCenterApp}, name='Studeleted'),

    url(r'approved/$', Approved.as_view(),
        {'model': StuActCenterApp}, name='Stuapproved'),

    url(r'^apply/meeting_room/$', ApplyRoomView.as_view(),
        {'appform': MroomAppForm,
         'model': MroomApp,
         'name': 'Mroomapply'}, name='Mroomapply'),

    url(r'^list/meeting_room/$', ListAppView.as_view(),
        {'model': MroomApp,
         'title': u'会议室使用申请',
         'name': 'Mroommanage'}, name='Mroomlist'),

    url(r'^table/meeting_room/$', Table.as_view(),
        {'model': MroomApp,
         'template': 'mroom_table.html',
         'name': 'mroom'}, name='Mroomtable'),

    url(r'^manage/meeting_room/$', ManageView.as_view(),
        {'model': MroomApp,
         'title': u'会议室使用申请',
         'name1': 'Mroommodify',
         'name2': 'Mroomdeleted',
         'name3': 'Mroomapproved'}, name='Mroommanage'),

    url(r'^modify/meeting_room/$', ModifyView.as_view(),
        {'appform': MroomAppForm,
         'model': MroomApp,
         'name': 'Mroommodify'}, name='Mroommodify'),

    url(r'deleted/$', Delete.as_view(),
        {'model': MroomApp}, name='Mroomdeleted'),

    url(r'approved/$', Approved.as_view(),
        {'model': MroomApp}, name='Mroomapproved'),
)
