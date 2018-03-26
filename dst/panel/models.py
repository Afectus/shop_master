from django.db import models

from PIL import Image
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit, SmartResize, Transpose, Adjust

from django.db.models.signals import post_delete, post_save
from django.db.models.signals import pre_delete

from django.contrib.auth.models import User, Group, UserManager

from django.core.validators import MinValueValidator, MaxValueValidator

import datetime
from django.utils import timezone

from node.models import *


#База изображений
class imagebase(models.Model):
	id = models.AutoField(primary_key=True, unique=True, verbose_name='id')
	ctime = models.DateTimeField(verbose_name=u'Дата', auto_now_add=True)
	title = models.CharField(verbose_name=u'Заголовок', help_text='Заголовок', max_length=200)

	#pict
	pict = models.ImageField(verbose_name=u'Картинка', upload_to=make_upload_path, max_length=300)
	pict100 = ImageSpecField(source='pict', processors=[ResizeToFit(100, 100)], format='PNG', options={'quality': 75})
	pict200 = ImageSpecField(source='pict', processors=[ResizeToFit(200, 200)], format='PNG', options={'quality': 75})
	pict300 = ImageSpecField(source='pict', processors=[ResizeToFit(300, 300)], format='PNG', options={'quality': 75})
	
	def __str__(self):
		return u'%s' % (self.id)

	class Meta:
		ordering=['-id']
		verbose_name = u'База изображений'
		verbose_name_plural = u'База изображений'		
		
		