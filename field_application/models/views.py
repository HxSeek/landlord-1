#-*- coding: utf-8 -*-
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class ApplyRoomView(View):
    
    
    @method_decorator(login_required)
    def get(self, request, **kwargs):
         return render(request, 'room/form.html', 
                               {'form': kwargs['form'](),
                                'post_url': reverse('models:%s') % kwargs['name'] })

    @method_decorator(login_required)
    def post(self, request, **kwargs):
        form = kwargs['form'](request.POST)
        if not form.is_valid():
            return render(request, 'room/form.html', 
                                  {'form': form(),
                                   'post_url': reverse('models:%s') % kwargs['name'] })
        form.save()
        return HttpResponseRedirect(reverse('home'))


class ListView(View):     
    
    def manage_list(request, **kwargs):
        app = kwargs['model'].objects.all()
        paginator = Paginator(app, 6)
        page = request.GET.get('page')
     
        try:
            page = paginator.page(page)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
    
        return render(request, 'room/list.html', {'page': page})


class ModifyView(View):

    @method_decorator(login_required)
    def get(self, request, **kwargs):
      app_id = request.GET.get('id')
      app = get_object_or_404(kwargs['model'], id=app_id)
      form = kwargs['form'](instance=app)
      return render(request, 'mroom/form.html',
                            {'form': form(), 'app_id': app_id,
                             'post_url': reverse('models:%s') % kwargs['name'] +'?id='+app_id})
    
    @method_decorator(login_required)
    def post(self, request, **kwargs):
      app_id = request.GET.get('id')
      app = get_object_or_404(kwargs['model'], id=app_id)
      form = kwargs['form'](request.POST, instance=app)
      if not form.is_valid():
          return render(request, 'mroom/form.html', 
                                {'form': form(), 'app_id': app_id, 
                                 'post_url': reverse('models:%s') % kwargs['name'] +'?id='+app_id})
      form.save()
      return HttpResponseRedirect(reverse('home'))
