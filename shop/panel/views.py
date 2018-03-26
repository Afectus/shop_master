from __future__ import unicode_literals
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponsePermanentRedirect

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.decorators.csrf import csrf_exempt

from django.utils.safestring import mark_safe

from django.core.exceptions import PermissionDenied

from django import forms
from django.core.exceptions import ValidationError
from django.contrib import auth
from django.contrib.auth.models import User, Group

from django.urls import reverse

import json
from django.core import serializers

from django.http import QueryDict

from django.views.generic import DetailView, ListView, DeleteView
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.views.generic.base import TemplateView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils.decorators import method_decorator

import datetime, time


from django.db.models import Max, Sum, Count
from django.db.models import Q, F

from ckeditor.widgets import CKEditorWidget

from dj.views import *


from django.core.mail import send_mail


from node.templatetags.nodetag import *

from node.models import *
from acl.models import *
from panel.form import *
from panel.models import *
from log.models import *
from acl.views import get_object_or_denied


import logging
log = logging.getLogger(__name__)




class index_panel(TemplateView):
	template_name = "index_panel.html"

	def dispatch(self, request, *args, **kwargs):
		return super(index_panel, self).dispatch(request, *args, **kwargs)
	
	def get_context_data(self, *args, **kwargs):
		context_data = super(index_panel, self).get_context_data(*args, **kwargs)
		#context_data.update({'goodfix': goodfix.objects.filter(status='open').order_by('-id')})
		return context_data


	
@csrf_exempt
def checkbackurl(request, backurl):
	if request.method == 'GET':
		data = smsqsend.objects.filter(back=False, backurl=backurl)
		if data.exists():
			data.update(back=True)
			tmp={'res': 1}
			return HttpResponse(json.dumps(tmp), content_type='application/json')
	tmp={'res': 0, 'data': u'bad',}
	return HttpResponse(json.dumps(tmp), content_type='application/json')
	
	
class user_password(FormView):
	template_name = 'user_password.html'
	form_class = Form_change_password
	success_url = "/user/login?passwd=change"

	def form_valid(self, form):
		cd = form.cleaned_data
		u = User.objects.get(id__exact=self.request.user.id)
		u.set_password(cd['password'])
		u.save()
		auth.logout(self.request)
		return super(user_password, self).form_valid(form)
		

@permission_required('node.add_buyer')
def getphone(request, pk):
	if request.method == 'GET':
		b=get_object_or_404(buyer, id=pk)
		res={'res': 1, 'phone': b.phone}
		return HttpResponse(json.dumps(res), content_type='application/json')

	res={'res': 0, 'data': u'Ошибка',}
	return HttpResponse(json.dumps(res), content_type='application/json')
		

#Редактировать собственный профиль пользователя		
class own_user_profile_edit(UpdateView):
	model = profileuser
	template_name = 'own_user_profile_edit.html'
	success_url = '/user/profile'
	fields = ['photo', 'position', 'phonemobile', 'phonework', ]
	
	def dispatch(self, request, *args, **kwargs):
		self.e = get_object_or_404(self.model, user=request.user)
		return super(own_user_profile_edit, self).dispatch(request, *args, **kwargs)
	
	#def get_success_url(self):
	#	return '/user/profile/%s' % (self.get_object().id)
	
	def get_object(self, queryset=None):
		return get_object_or_404(self.model, user=self.request.user)
	
	def get_context_data(self, **kwargs):
		context = super(own_user_profile_edit, self).get_context_data(**kwargs)
		context['object'] = self.get_object()
		return context
		
		
		
class user_restore(FormView):
	template_name = 'restore.html'
	success_url = '/user/login?send=true'
	form_class = Form_user_restore
	
	def dispatch(self, request, *args, **kwargs):
		#self.data = get_object_or_404(sticker, id=self.kwargs['pk'], status=True)
		#проверяем на наличие купона на изминение стикера
		#o = order.objects.filter(user=request.user, coupon__type__exact='sticker', status__exact='paid').first()
		#if not o:
		#	c = coupon.objects.get(type__exact='sticker')
		#	return HttpResponseRedirect('/order/%s' % c.id)
		return super(user_restore, self).dispatch(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(user_restore, self).get_context_data(**kwargs)
		#context['nickname'] = self.data.name
		return context
		
	def form_valid(self, form):
		cd = form.cleaned_data
		p=profileuser.objects.get(phone=cd['phone'])
		newpass = password_generator()
		p.user.set_password(newpass)
		p.user.save()
		sms4b(None, '8%s' % cd['phone'], 'login: %s pass: %s' % (p.user.username, newpass))
		
		#удаляем предыдущие связи
		#d = stickerowner.objects.filter(user=self.request.user, nickname=cd['nickname']).delete()
		#создаем новую
		#c = stickerowner.objects.create(user=self.request.user, nickname=cd['nickname'], sticker=cd['sticker'])
		#гасим купон
		#order.objects.filter(user=self.request.user, coupon__type__exact='sticker', status__exact='paid').update(status='used', desc2='changesticker to %s' % self.kwargs['pk'])
		return super(user_restore, self).form_valid(form)
		

@permission_required('panel.delete_imagebase')
def imagebase_del(request, pk):
	tmp={'res': 0, 'data': u'Ошибка',}
	if request.method == 'POST' or request.method == 'GET':
		try:
			data=imagebase.objects.get(id=pk)
		except:
			tmp={'res': 0, 'data': 'error',}
		else:
			data.delete()
			tmp={'res': 1, 'data': 'delete',}
	return HttpResponse(json.dumps(tmp), content_type='application/json')	
		
