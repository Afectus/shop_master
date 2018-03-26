# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import auth
from django.shortcuts import HttpResponseRedirect
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

from django.views.generic.base import TemplateView
from django.views.generic import RedirectView

from django.shortcuts import render_to_response, render

from .views import *
from .buyer import *
from .goods import *
from .goods_json import *
from .api import *



class saveonclose(TemplateView):
	template_name = '_saveonclose.html'

app_name = 'panel'
urlpatterns = [
	#url(r'^shop/list/?$', login_required(shop_list.as_view()), name='shop_list'),
	#url(r'^shop/edit/(?P<pk>\d+)/?$', login_required(shop_edit.as_view()), name='shop_edit'),
	#
	#url(r'^user/restore/?$', user_restore.as_view()),
	#url(r'^user/profile/?$', login_required(own_user_profile_edit.as_view())),
	#url(r'^user/password/?$', login_required(user_password.as_view())),
	#
	#url(r'^form/saveonclose/?$', login_required(saveonclose.as_view()), name='saveonclose'),
	#imagebase
	#url(r'^imagebase/del/(?P<pk>\d+)/?$', login_required(imagebase_del), name='imagebase_del'),
]





