#-*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget
from django.forms import Textarea

from field_application.student_activity_center.models \
        import StudentActivityCenterApplication


class StudentActivityCenterApplicationForm(ModelForm):

    class Meta:
        model = StudentActivityCenterApplication
        exclude = ['organization', 'approved', 'application_time']
        widgets = {
            'activity_summary': Textarea(),
        }

