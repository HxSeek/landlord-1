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
    def get(self, request, **kwargs):
        name = kwargs['name']
        return render(request, 'room/form.html',
                      {'form': kwargs['appform'],
                       'post_url': reverse('common:%s' % name)})

    @method_decorator(login_required)
    def post(self, request, **kwargs):
        form = kwargs['appform'](request.POST)
        model = kwargs['model']
        name = kwargs['name']
        if not form.is_valid():
            return render(request, 'room/form.html',
                          {'form': form,
                           'post_url': reverse('common:%s' % name)})
        model = form.save(commit=False)
        model.organization = request.user.organization
        model.submit()
        return HttpResponseRedirect(reverse('home'))


class Table(View):

    def get(self, request, **kwargs):
        name = kwargs['name']
        model = kwargs['model']
        field = Field.objects.get(name__exact=name)
        table = field.generate_table(model)
        return render(request, kwargs['template'], {'table': table})


def generate_page(listing, request):
    paginator = Paginator(listing, 40)
    try:
        page = paginator.page(request.GET.get('page'))
    except InvalidPage:
        page = paginator.page(1)
    return page


class ListAppView(View):

    def get(self, request, **kwargs):
        model = kwargs['model']
        name = kwargs['name']
        listing = model.objects.all().order_by('id')

        return render(request, 'room/list.html',
                               {'manage_url': reverse('common:%s' % name),
                                'page': generate_page(listing, request),
                                'title': kwargs['title'],
                                'form': SearchForm()})

    def post(self, request, **kwargs):
        form = SearchForm(request.POST)
        model = kwargs['model']
        name = kwargs['name']
        if not form.is_valid():
            listing = model.objects.all().order_by('id')
        else:
            listing = search_application(model, form).order_by('id')

        return render(request, 'list.html',
                               {'manage_url': reverse('common:%s' % name),
                                'page': generate_page(listing, request),
                                'title': kwargs['title'],
                                'form': form})


class ManageView(View):

    @method_decorator(login_required)
    def get(self, request, **kwargs):
        model = kwargs['model']
        return ManageView.manage(request, SearchForm(),
                                 model.objects.all(),
                                 kwargs['title'],
                                 kwargs['mname'],
                                 kwargs['dname'],
                                 kwargs['aname'])

    @method_decorator(login_required)
    def post(self, request, **kwargs):
        form = SearchForm(request.POST)
        model = kwargs['model']
        if not form.is_valid():
            listing = \
                model.objects.all().order_by('id')
        else:
            listing = search_application(model, form)

        return ManageView.manage(request, form,
                                 listing, kwargs['title'],
                                 kwargs['mname'],
                                 kwargs['dname'],
                                 kwargs['aname'])

    @classmethod
    def manage(cls, request, form, listing, title, mname, dname, aname):
        listing = listing.order_by('id')
        page = generate_page(listing, request)

        return render(request, 'manage.html', {'page': page,
                               'title': title,
                               'modify_url': reverse('common:%s' % mname),
                               'approve_url': reverse('common:%s' % aname),
                               'delete_url': reverse('common:%s' % dname),
                               'form': form})


class ModifyView(View):

    @method_decorator(login_required)
    def get(self, request, **kwargs):
        app_id = request.GET.get('id')
        model = kwargs['model']
        name = kwargs['name']
        app = get_object_or_404(model, id=app_id)
        form = kwargs['appform'](instance=app)
        post_url = reverse('common:%s?id=%d' % (name, app_id))

        return render(request, 'room/form.html',
                      {'form': form, 'post_url': post_url})

    @method_decorator(login_required)
    def post(self, request, **kwargs):
        app_id = request.GET.get('id')
        model = kwargs['model']
        name = kwargs['name']
        app = get_object_or_404(model, id=app_id)
        form = kwargs['appform'](request.POST, instance=app)
        if not form.is_valid():
            post_url = reverse('common:%s?id=%d' % (name, app_id))
            return render(request, 'room/form.html',
                          {'form': form, 'post_url': post_url})
        model = form.save(commit=False)
        model.submit()
        return HttpResponseRedirect(reverse('home'))


class Delete(View):
    @method_decorator(login_required)
    def get(self, request, **kwargs):
        app_id = request.GET.get('id')
        model = kwargs['model']
        name = kwargs['name']
        app = get_object_or_404(model, id=app_id)
        app.delete()
        return HttpResponseRedirect(reverse('common:%s' % name))


class Approved(View):
    @method_decorator(login_required)
    def get(self, request, **kwargs):
        app_id = request.GET.get('id')
        model = kwargs['model']
        name = kwargs['name']
        app = get_object_or_404(model, id=app_id)
        app.approved = not app.approved
        app.submit()
        return HttpResponseRedirect(reverse('common:%s' % name))
