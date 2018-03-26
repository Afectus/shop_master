# -*- coding: utf-8 -*-
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
from acl.views import get_object_or_denied


import logging
log = logging.getLogger(__name__)




class home(TemplateView):
	template_name = "index.html"

	def dispatch(self, request, *args, **kwargs):
		return super(home, self).dispatch(request, *args, **kwargs)
	
	def get_context_data(self, *args, **kwargs):
		context_data = super(home, self).get_context_data(*args, **kwargs)
		#context_data.update({'goodfix': goodfix.objects.filter(status='open').order_by('-id')})
		
		return context_data


class tax_list(ListView): 
	template_name = 'tax_list.html' 
	model = tax
	# paginate_by = 6

	def dispatch(self, request, *args, **kwargs): 
		return super(tax_list, self).dispatch(request, *args, **kwargs) 

	def get_queryset(self): 
		data=super(tax_list, self).get_queryset() 
		data = data.filter(status=True).filter(parent=None).filter(showonsite=True) #for get_context_data 
		return data 

class goods_list(ListView): 
	template_name = 'goods_list.html' 
	model = goods
	# paginate_by = 6

	def dispatch(self, request, *args, **kwargs): 
		self.data = get_object_or_404(tax, hurl=self.kwargs['pk'])
		return super(goods_list, self).dispatch(request, *args, **kwargs) 

	def get_queryset(self):
		
		paging = 20

		data=super(goods_list, self).get_queryset() 
		data = data.filter(Q(tax=self.data) | Q(tax__parent=self.data)) #for get_context_data

		#paginator
		self.p = Paginator(data, paging)
		#page = self.kwargs['page']
		xpage = self.request.GET.get('xpage', default=1)
		#print self.p.number()
		try:
			pdata = self.p.page(xpage)
		except PageNotAnInteger:
			# If page is not an integer, deliver first page.
			pdata = self.p.page(1)
		except EmptyPage:
			# If page is out of range (e.g. 9999), deliver last page of results.
			pdata = self.p.page(self.p.num_pages)	

		return pdata

	def get_context_data(self, *args, **kwargs):
		context_data = super(goods_list, self).get_context_data(*args, **kwargs)
		context_data.update({'object': self.data})
		context_data.update({'count': self.p.count,})
		context_data.update({'urlpage': reverse('shopapp:goods_list', args=[self.data.hurl]),})
		return context_data
