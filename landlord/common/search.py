#-*- coding: utf-8 -*-
from django import forms
from landlord.mroom.models import MroomApp


class SearchForm(forms.Form):

    SEARCH_CHOICES = (
        ('org', u'申请组织'),
        ('title', u'活动标题'),
        ('place', u'活动地点'),
    )

    APPROVED_CHOICES = (
        ('all', u'全部'),
        ('yes', u'已批准'),
        ('no', u'未批准'),
    )

    search_type = forms.ChoiceField(choices=SEARCH_CHOICES)
    search_value = forms.CharField(max_length=40, required=False)
    approved = forms.ChoiceField(choices=APPROVED_CHOICES)


def search_application(model, form):
    search_type = form.cleaned_data['search_type']
    search_value = form.cleaned_data['search_value']
    approved_value = form.cleaned_data['approved']

    search_value = '%' + '%'.join(search_value) + '%'
    if search_type == 'org':
        apps = model.objects.filter(
            organization__chinese_name__exact=search_value)
    elif search_type == 'title':
        if model == MroomApp:
            apps = model.objects.filter(meeting_topic__exact=search_value)
        else:
            apps = model.objects.filter(activity__exact=search_value)
    elif search_type == 'place':
            apps = model.objects.filter(place__name__exact=search_value)
    else:
        raise Exception('search_type is not valid')
'''
    if approved_value == 'all':
        return apps
    elif approved_value == 'yes':
        return apps.filter(approved=True)
    elif approved_value == 'no':
        return apps.filter(approved=False)
    else:
        raise Exception('approved_value is not valid')
'''
