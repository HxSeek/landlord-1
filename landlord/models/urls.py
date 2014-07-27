from django.conf.urls import url, patterns

from .views import ApplyRoomView, ListView, ModifyView

from landlord.student_activity_center.forms import StudentActivityCenterApplicationForm
from landlord.student_activity_center.models import StudentActivityCenterApplication

urlpatterns = patterns(
    '',
    url(r'^apply/student_activity_center/$', ApplyRoomView.as_view(),
               { 'appform' : StudentActivityCenterApplicationForm, 
                 'model' : StudentActivityCenterApplication }, name='Stuapply'),

    url(r'^list/student_activity_center/$', ListView.as_view(), 
    	       { 'model' : StudentActivityCenterApplication }, name='Stulist'),

    url(r'^modify/student_activity_center/$', ModifyView.as_view(),
               { 'appform' : StudentActivityCenterApplicationForm,
                 'model' : StudentActivityCenterApplication }, name='Stumodify'),
    )
    
   
