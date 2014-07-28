from django.conf.urls import url, patterns

from .views import ApplyRoomView, ListView, ModifyView

from landlord.stu_act.forms import StuActCenterApplyForm
from landlord.stu_act.models import StuActCenterApply


urlpatterns = patterns(
    '',
    url(r'^apply/student_activity_center/$', ApplyRoomView.as_view(),
        {'appform': StuActCenterApplyForm,
         'model': StuActCenterApply}, name='Stuapply'),

    url(r'^list/student_activity_center/$', ListView.as_view(),
        {'model': StuActCenterApply}, name='Stulist'),

    url(r'^modify/student_activity_center/$', ModifyView.as_view(),
        {'appform': StuActCenterApplyForm,
         'model': StuActCenterApply}, name='Stumodify'),
)
