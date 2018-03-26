## оформление кода

#### приложение 

шаблон имени: **xxxxapp**

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

#### модель: 

шаблон имени: **xxxxitem**, **xxxxlist**, **xxxxs**

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

***

#### управление элементами admin.py

пример:

```python
from .models import *

class newslistAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'name', 'pict',)
admin.site.register(newslist, newslistAdmin)
```

***

#### управление элементами panel.py

шаблон наименования класса

- список элементов: panel_названиемодели_list(ListView)
- добавление элемента: panel_названиемодели_add(CreateView)
- удаление элемента: panel_названиемодел_del(DeleteView)
- редактирование элемента: panel_названиемодел_edit(UpdateView)


пример:

```python
from acl.views import get_object_or_denied
#(('A', 'All'), ('L', 'Список'), ('R', 'Чтение'), ('C', 'Создание'), ('U', 'Редактирование'),)

class panel_newslist_list(ListView):
	model = newslist
	template_name = 'panel_newslist_list.html'

	def dispatch(self, request, *args, **kwargs):
		get_object_or_denied(self.request.user, 'newslist', 'L') #проверяем права
		return super(panel_newslist_list, self).dispatch(request, *args, **kwargs)
		
		
class panel_newslist_add(CreateView):
	model = newslist
	template_name = 'panel_newslist_add.html'
	fields = ['name', 'pict']

	def dispatch(self, request, *args, **kwargs):
		get_object_or_denied(self.request.user, 'newslist', 'C') #проверяем права
		return super(panel_newslist_add, self).dispatch(request, *args, **kwargs)

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		instance.save()
		self.data = instance
		return super(panel_newslist_add, self).form_valid(form)

	def get_success_url(self):
		return reverse_lazy('panel_newslist_list')
		

class panel_newslist_del(DeleteView):
	model = newslist
	template_name = 'panel_newslist_del.html'

	def dispatch(self, request, *args, **kwargs):
		get_object_or_denied(self.request.user, 'baner', 'U') #проверяем права
		return super(panel_newslist_del, self).dispatch(request, *args, **kwargs)

	def get_success_url(self):
		return reverse_lazy('panel_newslist_list')
		
		
class panel_newslist_edit(UpdateView):
	model = newslist
	template_name = 'panel_newslist_edit.html'
	fields = ['url', 'pict']

	def dispatch(self, request, *args, **kwargs):
		get_object_or_denied(self.request.user, 'baner', 'U') #проверяем права
		return super(panel_newslist_edit, self).dispatch(request, *args, **kwargs)

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		instance.save()
		self.data = instance
		return super(panel_newslist_edit, self).form_valid(form)

	def get_success_url(self):
		return reverse_lazy('panel_newslist_list')
		
```



