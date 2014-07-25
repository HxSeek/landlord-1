#-*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget
from django.forms import Textarea

from .models import StudentActivityCenterApplication


class StudentActivityCenterApplicationForm(ModelForm):

    class Meta:
        model = StudentActivityCenterApplication
        exclude = ['organization', 'application_time', 'approved', 'deleted']
        widgets = {
            'date' : SelectDateWidget(),
            'activity_summary' : Textarea(),
        }
