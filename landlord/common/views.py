# -*- coding: utf-8 -*-
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.paginator import InvalidPage, Paginator

from landlord.common.models import Field
from landlord.common.search import SearchForm
from landlord.common.search import search_application


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


class Table(View):

    def get(self, request, model, template, name):
        field = Field.objects.get(name__exact=name)
        table = field.generate_table(model)
        return render(request, template, {'table': table})


def generate_page(listing, request):
    for app in listing:
        app.date = app.date.strftime('%Y年%m月%d日')
    paginator = Paginator(listing, 40)
    try:
        page = paginator.page(request.GET.get('page'))
    except InvalidPage:
        page = paginator.page(1)
    return page


class ListAppView(View):

    def get(self, request, model, title, name):
        listing = model.objects.all().order_by('id')
        return render(request, 'room/list.html',
                               {'manage_url': reverse('common:%s' % name),
                                'page': generate_page(listing, request),
                                'title': title,
                                'form': SearchForm()})

    def post(self, request, model, title, name):
        form = SearchForm(request.POST)
        if not form.is_valid():
            listing = model.objects.all().order_by('id')
        else:
            listing = search_application(model, form).order_by('id')
        return render(request, 'list.html',
                               {'manage_url': reverse('common:%s' % name),
                                'page': generate_page(listing, request),
                                'title': title,
                                'form': form})


class ManageView(View):

    @method_decorator(login_required)
    def get(self, request, model, title, name1, name2, name3):
        return ManageView.manage(request, model.objects.all(),
                                 SearchForm(), title, name1, name2, name3)

    @method_decorator(login_required)
    def post(self, request, model, title, name1, name2, name3):
        form = SearchForm(request.POST)
        if not form.is_valid():
            listing = \
                model.objects.all().order_by('id')
        else:
            listing = search_application(model, form)

        return ManageView.manage(request, listing, form, title, name1,
                                 name2, name3)

    @classmethod
    def manage(cls, request, listing, form, title, name1,
               name2, name3):
        listing = listing.order_by('id')
        page = generate_page(listing, request)
        return render(request, 'manage.html', {'page': page,
                               'title': title,
                               'modify_url': reverse('common:%s' % name1),
                               'approve_url': reverse('common:%s' % name2),
                               'delete_url': reverse('common:%s' % name3),
                               'form': form})


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


class Delete(View):
    @method_decorator(login_required)
    def delete(self, request, model):
        app_id = request.GET.get('id')
        app = get_object_or_404(model, id=app_id)
        app.delete()
        return HttpResponseRedirect(reverse('common:deleted'))


class Approved(View):
        @method_decorator(login_required)
        def manager_approve(self, request, model):
            app_id = request.GET.get('id')
            app = get_object_or_404(model, id=app_id)
            app.approved = not app.approved
            app.submit()
            return HttpResponseRedirect(reverse('common:approved'))
