# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response



from django.db.models import Sum, Q, F, Count, TextField
from django.db.models.functions import Cast

from django.utils.safestring import mark_safe
from django.utils.numberformat import format

from django.contrib.auth.models import User, Group, UserManager

import re, datetime

from django import template

register = template.Library()


from node.models import *

@register.simple_tag
def sidebar_obj(tax_item_selected):
	parent = tax.objects.filter(status=True).order_by('idbitrix')
	child = []
	if tax_item_selected.parent is None:
		child = tax.objects.filter(parent=tax_item_selected).order_by('idbitrix')
		# print(child)
	else:
		child = tax.objects.filter(parent=tax_item_selected.parent).order_by('idbitrix')
		# print(child)

	return [parent, child]

@register.simple_tag
def goods_in_stock(good):
	obj = goodsinstock.objects.filter(goods=good)
	return obj

@register.simple_tag
def goods_property_list(goods):
	data=properties.objects.filter(status=True, propertiesvalue__goods=goods).distinct()
	return data
