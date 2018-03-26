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

app_name = 'shopapp'
urlpatterns = [
	url(r'^$', home.as_view()),
	url(r'^katalog/?$', login_required(tax_list.as_view()), name='tax_list'),
	url(r'^katalog/(?P<pk>\w+)/?$', login_required(goods_list.as_view()), name='goods_list'),
]





