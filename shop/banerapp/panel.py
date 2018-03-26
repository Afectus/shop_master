from .models import *
from django.views.generic.edit import CreateView, DeleteView, UpdateView ,FormView
from django.views.generic import ListView,DetailView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from acl.views import get_object_or_denied
# Create your views here.


# Менеджмент вьюхи

class panel_baneritem_list(ListView):
	model = baneritem
	template_name = 'panel_baneritem_list.html'
	#context_object_name = 'context_list_baneritem'

	def dispatch(self, request, *args, **kwargs):
		get_object_or_denied(self.request.user, 'baner', 'L') #проверяем права
		return super(panel_baneritem_list, self).dispatch(request, *args, **kwargs)

class panel_baneritem_add(CreateView):
	model = baneritem
	template_name = 'panel_baneritem_add.html'
	fields = ['url', 'pict']


	def dispatch(self, request, *args, **kwargs):
		get_object_or_denied(self.request.user, 'baner', 'C') #проверяем права
		return super(panel_baneritem_add, self).dispatch(request, *args, **kwargs)

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		instance.save()
		self.data = instance
		return super(panel_baneritem_add, self).form_valid(form)

	def get_success_url(self):
		return reverse_lazy('panel_baneritem_list')
	

class panel_baneritem_del(DeleteView):
	model = baneritem
	template_name = 'panel_baneritem_del.html'


	def dispatch(self, request, *args, **kwargs):
		get_object_or_denied(self.request.user, 'baner', 'R') #проверяем права
		return super(panel_baneritem_del, self).dispatch(request, *args, **kwargs)


	def get_success_url(self):
		return reverse_lazy('panel_baneritem_list')
		


class panel_baneritem_edit(UpdateView):
	model = baneritem
	template_name = 'panel_baneritem_edit.html'
	fields = ['url', 'pict']

	def dispatch(self, request, *args, **kwargs):
		get_object_or_denied(self.request.user, 'baner', 'L') #проверяем права
		return super(panel_baneritem_edit, self).dispatch(request, *args, **kwargs)

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		instance.save()
		self.data = instance
		return super(panel_baneritem_edit, self).form_valid(form)

	def get_success_url(self):
		return reverse_lazy('panel_baneritem_list')