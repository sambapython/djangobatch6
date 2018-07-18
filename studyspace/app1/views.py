# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from app1.models import StudyHall, Expenses, Enquiry

# Create your views here.
def view_index(request):
	if request.method=="POST":
		data = request.POST
		hall = StudyHall(name=data.get("hall_name"), 
			area=data.get("hall_area"))
		hall.save()
	studyhalls = StudyHall.objects.all()
	expenses = Expenses.objects.all()
	enquiries = Enquiry.objects.all()
	return render(request,"app1/index.html",{
		"halls": studyhalls,
		"exps": expenses,
		"enqs": enquiries 
		})
def view_syudyhalls(request):
	studyhalls = StudyHall.objects.all()
	return render(request,"app1/index.html",{"studyhalls":studyhalls})
