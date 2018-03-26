from django.contrib import admin
from django.urls import path, include, re_path

from django.contrib.auth.decorators import login_required, permission_required

from .views import *
from .panel import *

urlpatterns = [
	#panel
	re_path('^panel/baneritem/list/?$', login_required(panel_baneritem_list.as_view()), name='panel_baneritem_list'),
	re_path('^panel/baneritem/add/?$', login_required(panel_baneritem_add.as_view()), name='panel_baneritem_add'),
	re_path('^panel/baneritem/del/(?P<pk>\d+)/?$', login_required(panel_baneritem_del.as_view()), name='panel_baneritem_del'),
	re_path('^panel/baneritem/edit/(?P<pk>\d+)/?$', login_required(panel_baneritem_edit.as_view()), name='panel_baneritem_edit'),
]
