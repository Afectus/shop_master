from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea

from panel.models import *


class imagebaseAdmin(admin.ModelAdmin):
	list_display = ('id', 'ctime', 'title', 'pict', )
admin.site.register(imagebase, imagebaseAdmin)
