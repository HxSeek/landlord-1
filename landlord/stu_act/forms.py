# -*- coding: utf-8 -*-
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.forms import Textarea

from .models import StuActCenterApp


class StuActCenterAppForm(forms.ModelForm):

    class Meta:
        model = StuActCenterApp
        exclude = ['organization', 'application_time', 'approved', 'deleted']
        widgets = {
            'date': SelectDateWidget(),
            'activity_summary': Textarea(),
        }
