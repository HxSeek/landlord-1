# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget
from django.forms import Textarea

from .models import StuActCenterApp


class StuActCenterAppForm(ModelForm):

    class Meta:
        model = StuActCenterApp
        exclude = ['organization', 'application_time', 'approved', 'deleted']
        widgets = {
            'date': SelectDateWidget(),
            'activity_summary': Textarea(),
        }
