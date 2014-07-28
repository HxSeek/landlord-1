from django.conf.urls import url, patterns

from .views import ApplyRoomView, ListView, ModifyView

from landlord.stu_act.forms import StuActCenterAppForm
from landlord.stu_act.models import StuActCenterApp


urlpatterns = patterns(
    '',
    url(r'^apply/student_activity_center/$', ApplyRoomView.as_view(),
        {'appform': StuActCenterAppForm,
         'model': StuActCenterApp}, name='Stuapply'),

    url(r'^list/student_activity_center/$', ListView.as_view(),
        {'model': StuActCenterApp}, name='Stulist'),

    url(r'^modify/student_activity_center/$', ModifyView.as_view(),
        {'appform': StuActCenterAppForm,
         'model': StuActCenterApp}, name='Stumodify'),
)
