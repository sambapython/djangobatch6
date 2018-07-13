# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Customer	

# Create your views here.
def sales(request):
	return render(request,"app1/sales.html")
def products(request):
	return render(request,"app1/product.html")
def customers(request):
	#return HttpResponse("customers")
	'''
	list_customer = ["anil","ashok","pavan","aleka"]
	message="showing customers successfully"
	return render(request,"app1/customer.html",{"data":list_customer,
		"msg": message})
	'''
	customers = Customer.objects.all()
	return render(request,"app1/customer.html",{"data":customers})

