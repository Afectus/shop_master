from django.contrib import admin

from .models import *

class BaneritemAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'url', 'pict',)
	#list_filter = ('user', )

admin.site.register(baneritem, BaneritemAdmin)