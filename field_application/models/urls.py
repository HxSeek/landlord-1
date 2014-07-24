from django.conf.urls import url, patterns

from .views import ApplyRoomView, ListView, ModifyView

from field_application.student_activity_center.forms import StudentActivityCenterApplicationForm
from field_application.student_activity_center.models import StudentActivityCenterApplication

urlpatterns = patterns(
    '',
    url(r'^apply/$', ApplyRoomView.as_view(),
               { 'form' : StudentActivityCenterApplicationForm,
                 'name' : 'Stuapply' }, name='Stuapply'),

    url(r'^list/$', ListView.as_view(), 
    	       { 'model' : StudentActivityCenterApplication }, name='Stulist'),

    url(r'^modify/$', ModifyView.as_view(),
               { 'form' : StudentActivityCenterApplicationForm,
                 'model' : StudentActivityCenterApplication,
                 'name' : 'Stumodify' }, name='Stumodify'),
    )
    
   
