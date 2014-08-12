# -*- coding: utf-8 -*-
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from landlord.common.models import Field


class ApplyRoomView(View):

    @method_decorator(login_required)
    def get(self, request, appform, model, name):
        return render(request, 'room/form.html',
                      {'form': appform,
                       'post_url': reverse('common:%s' % name)})

    @method_decorator(login_required)
    def post(self, request, appform, model, name):
        form = appform(request.POST)
        if not form.is_valid():
            return render(request, 'room/form.html',
                          {'form': form,
                           'post_url': reverse('common:%s' % name)})
        model = form.save(commit=False)
        model.organization = request.user.organization
        model.submit()
        return HttpResponseRedirect(reverse('home'))


class table(View):

    def get(self, request, model, template, name):
        field = Field.objects.get(name__exact=name)
        table = field.generate_table(model)
        return render(request, template, {'table': table})


class ListView(View):

    def get(self, request, model, name):
        app = model.objects.all()
        paginator = Paginator(app, 6)
        page = request.GET.get('page')

        try:
            page = paginator.page(page)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)()

        return render(request, 'room/list.html', {'page': page, 'name': name})


class ModifyView(View):

    @method_decorator(login_required)
    def get(self, request, appform, model, name):
        app_id = request.GET.get('id')
        app = get_object_or_404(model, id=app_id)
        form = appform(instance=app)
        post_url = reverse('common:%s' % name) + '?id=' + app_id
        return render(request, 'room/form.html',
                      {'form': form, 'app_id': app_id,
                       'post_url': post_url})

    @method_decorator(login_required)
    def post(self, request, appform, model, name):
        app_id = request.GET.get('id')
        app = get_object_or_404(model, id=app_id)
        form = appform(request.POST, instance=app)
        if not form.is_valid():
            post_url = reverse('common:%s' % name) + '?id=' + app_id
            return render(request, 'room/form.html',
                          {'form': form, 'app_id': app_id,
                           'post_url': post_url})
        model = form.save(commit=False)
        model.submit()
        return HttpResponseRedirect(reverse('home'))
