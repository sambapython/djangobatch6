# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.forms.widgets import DateTimeInput
from .models import SalesOrder

# Create your views here.
# def index_view(request):
# 	return render(request,"app1/index.html")
class SaleCreateview(CreateView):
	class Meta:
		model=SalesOrder
		success_url="/saleorders/"
		fields="__all__"
	
	def __init__(self, *args, **kwargs):
		super(SaleCreateview,self).__init__(*args, **kwargs)
		#self.fields['date'].widget = DateTimeInput
	# def get_form(request):
	# 	import pdb; pdb.set_trace()