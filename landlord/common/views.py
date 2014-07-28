# -*- coding: utf-8 -*-
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class ApplyRoomView(View):

    @method_decorator(login_required)
    def get(self, request, appform, model):
        return render(request, 'room/form.html',
                      {'form': appform,
                       'post_url': reverse('common:Stuapply')})

    @method_decorator(login_required)
    def post(self, request, appform, model):
        form = appform(request.POST)
        if not form.is_valid():
            return render(request, 'room/form.html',
                          {'form': form,
                           'post_url': reverse('common:Stuapply')})
        model = form.save(commit=False)
        model.organization = request.user.organization
        model.submit()
        return HttpResponseRedirect(reverse('home'))


class ListView(View):

    def get(self, request, model):
        app = model.objects.all()
        paginator = Paginator(app, 6)
        page = request.GET.get('page')

        try:
            page = paginator.page(page)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)()

        return render(request, 'room/list.html', {'page': page})


class ModifyView(View):

    @method_decorator(login_required)
    def get(self, request, appform, model):
        app_id = request.GET.get('id')
        app = get_object_or_404(model, id=app_id)
        form = appform(instance=app)
        post_url = reverse('common:Stumodify') + '?id=' + app_id
        return render(request, 'room/form.html',
                      {'form': form, 'app_id': app_id,
                       'post_url': post_url})

    @method_decorator(login_required)
    def post(self, request, appform, model):
        app_id = request.GET.get('id')
        app = get_object_or_404(model, id=app_id)
        form = appform(request.POST, instance=app)
        if not form.is_valid():
            post_url = reverse('common:Stumodify') + '?id=' + app_id
            return render(request, 'room/form.html',
                          {'form': form, 'app_id': app_id,
                           'post_url': post_url})
        model = form.save(commit=False)
        model.submit()
        return HttpResponseRedirect(reverse('home'))
