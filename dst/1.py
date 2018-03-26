#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os, django

projecthome = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if projecthome not in sys.path:
    sys.path.append(projecthome)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dj.settings")
django.setup()

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
from django.db.models import Min, Max, Sum, Count, Avg
from django.db.models import Q, F, Func, Value, IntegerField, FloatField, CharField, Case, When
from django.db.models.functions import Coalesce
from django.db.models.functions import Cast, Trunc, TruncMonth, ExtractYear, ExtractMonth, ExtractWeek, ExtractWeekDay, ExtractDay
from ckeditor.widgets import CKEditorWidget
from dj.views import *
from django.core.mail import send_mail
from node.templatetags.nodetag import *
from node.models import *

#c=Count(Case(When('motivationinpoints', then=1),output_field=FloatField(),))	
#c=Cast(Count('motivationinpoints'), FloatField())

# from django.db.models import OuterRef, Subquery


# s = goodsinstock.objects.filter(goods=OuterRef('pk')).order_by().values('value')
# ts = s.annotate(s=Sum('value')).values('value')

# data = goods.objects.filter(length__gt=Subquery(total_comments))





# for i in data:
	# print(i)

# data=goods.objects.all()


# data=data.annotate(s1=Coalesce(Sum('goodsinstock__value'), Value(0)))


# for i in data:
	# print(i.name, i.s1)

	
	
	
from django.db.models.expressions import RawSQL
data = goods.objects.raw("select * from node_goodsinstock inner join node_goods on node_goodsinstock.goods_id = node_goods.id inner join node_stock on node_goodsinstock.stock_id=node_stock.id WHERE value >0;")

for i in data:
	print(dir(i))
	

