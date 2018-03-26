from django.db import models

#Для сохранения картинок
import re
import random
# Для изменения размеров картинки
from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFill,ResizeToFit
from django.contrib.auth.models import User
# Create your models here.

from dj.views import *

class baneritem(models.Model):
	"""Модель для банеров"""
	id = models.AutoField(primary_key=True, unique=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	url = models.CharField(verbose_name = "Ссылка для банера", max_length=200)
	pict = models.ImageField(upload_to=make_upload_file, verbose_name = "Картинка для банера")
	pict40 = ImageSpecField(source='pict', processors=[ResizeToFit(40, 40)], format='PNG', options={'quality': 95})
	pict100 = ImageSpecField(source='pict', processors=[ResizeToFit(100, 100)], format='PNG', options={'quality': 95})

	def __str__(self):
		return u'%s' % (self.id)