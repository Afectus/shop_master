# Правила оформления кода

Имя приложения: xxxxapp
пример: newsapp


Имя модели: xxxxitem, xxxxlist xxxxs
пример: newsitem, newslist, newss




Загрузка картинок в модель при помощи функции make_upload_path или make_upload_file из dj.views

пример:
'''python
from dj.views import *

class newslist(models.Model):
	pict = models.ImageField(upload_to=make_upload_file, verbose_name="Изображение")
''''
