# -*- coding: utf-8 -*-
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.forms import Textarea

from .models import MroomApp


class MroomAppForm(forms.ModelForm):

    class Meta:
        model = MroomApp
        exclude = ['organization', 'application_time', 'approved', 'deleted']
        widgets = {
            'date': SelectDateWidget(),
            'meeting_summary': Textarea(),
            'remarks': Textarea(),
        }
