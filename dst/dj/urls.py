from django.contrib import admin
from django.urls import path

from django.conf.urls import include, url

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

def auth_logout(request):
	auth.logout(request)
	return HttpResponseRedirect("/user/login")
	
	
def getcap(request):
	from django.http import HttpResponse
	import json
	from captcha.models import CaptchaStore
	from captcha.helpers import captcha_image_url
	newcapkey = CaptchaStore.generate_key()
	newcapimg  = captcha_image_url(newcapkey)
	tmp={'res': 1, 'key': newcapkey, 'img': newcapimg,}
	return HttpResponse(json.dumps(tmp), content_type='application/json')
	

class test(TemplateView):
	template_name = 'test.html'
	
class test2(TemplateView):
	template_name = 'test2.html'
	
def my404(request):
	return render(request, '404.html', status=404)
	
def my500(request):
	return render(request, '500.html', status=500)

handler404 = my404
handler500 = my500
	
	

urlpatterns = [
	#include app urls
	url(r'^', include('acl.urls')),
	url(r'^', include('shopapp.urls')),
	#url(r'^', include('newsapp.urls')),
	#url(r'^', include('panel.urls')),
	#
	url(r'^test/?$', test.as_view()),
	url(r'^test2/?$', test2.as_view()),
	#
	url(r'^user/logout/?$', auth_logout),
	url(r'^getcap/?$', getcap),
	#
	url(r'^captcha/', include('captcha.urls')),
	path('admin/', admin.site.urls),
	#url(r'^i18n/', include('django.conf.urls.i18n')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_title = 'shop'
admin.site.site_header = 'shop'


# if settings.DEBUG:
	# import debug_toolbar
	# urlpatterns += [
		# url(r'^__debug__/', include(debug_toolbar.urls)),
	# ]


