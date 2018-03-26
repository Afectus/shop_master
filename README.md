## оформление кода

имя приложения: **xxxxapp**

пример:
```python
INSTALLED_APPS = [
	'shopapp',
	'banerapp',
	'newsapp',
	...
]
urlpatterns = [
	url(r'^', include('shopapp.urls')),
	url(r'^', include('banerapp.urls')),
	url(r'^', include('newsapp.urls')),
	...
```

***

модель: **xxxxitem**, **xxxxlist**, **xxxxs**

Загрузка картинок в модель при помощи функции **make_upload_path** или **make_upload_file** из **dj.views**

пример:
```python
from dj.views import *

class newslist(models.Model): #newslist, newss
	id = models.AutoField(primary_key=True, unique=True) #обязательное поле
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	name = models.CharField(verbose_name='Название', max_length=200)
	pict = models.ImageField(upload_to=make_upload_file, verbose_name='Изображение')
	pict40 = ImageSpecField(source='pict', processors=[ResizeToFit(40, 40)], format='PNG', options={'quality': 95})
	pict100 = ImageSpecField(source='pict', processors=[ResizeToFit(100, 100)], format='PNG', options={'quality': 95})

	def __str__(self):
		return u'%s' % (self.id, self.name)
```
