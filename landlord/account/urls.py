#-*- coding: utf-8 -*-
from django.conf.urls import url, patterns
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

from landlord.account.views import SignOutView, SignInView 
from landlord.account.views import SignUpView, ResetPasswordView


urlpatterns = patterns(
    '',
    url(r'^signin/$', SignInView.as_view(), name='signin'),
    url(r'^signup/$', SignUpView.as_view(), name='signup'),
    url(r'^signout/$', SignOutView.as_view(), name='signout'),
    url(r'^reset_password/$', ResetPasswordView.as_view(), 
        name='reset_password'),
 
 )
