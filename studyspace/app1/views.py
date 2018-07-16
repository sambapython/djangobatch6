# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from app1.models import StudyHall 

# Create your views here.
def view_index(request):
	return render(request,"app1/index.html")
def view_syudyhalls(request):
	studyhalls = StudyHall.objects.all()
	return render(request,"app1/index.html",{"studyhalls":studyhalls})
