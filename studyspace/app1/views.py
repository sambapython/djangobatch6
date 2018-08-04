# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from app1.models import StudyHall, Expenses, Enquiry, Course, Student,\
 Expenses, UserProfile
from django.contrib.auth import authenticate, login, logout

import os
from django.conf import settings
import time

from app1.forms import ExpensesForm

def ExpensesView(request):
	if request.method=="POST":
		form = ExpensesForm(request.POST)
		if form.is_valid():
			form.save()
		
	form = ExpensesForm()

	return render(request,"app1/expenses.html",
		{"form":form,"data":Expenses.objects.all()})



# Create your views here.
def view_index(request):

	if request.method=="POST":
		data = request.POST

		if data.get("reg"):
			up = UserProfile.objects.create_user(
				username=data.get("username"),
				password=data.get("password"),
				email = data.get("email")
				)
			return render(request,"app1/index.html",
				{"msg":"USER created successfully!!. Please login"})
		else:
			user = authenticate(
				username=data.get("username"),
				password=data.get("password")
				)
			if user:
				#request.session.update({"user":user.username})
				login(request, user)
				return render(request,"app1/home.html",
					{"msg":"Login success"})
			else:
				return render(request,"app1/index.html",
					{"msg": "Login failed."})

	return render(request,"app1/index.html")

def login_req(f, *args1):
	def inner(*args):
		if "_auth_user_id" in args[0].session:
			return f(*args)
		else:
			return redirect(view_index)
	return inner

@login_req
def view_syudyhalls(request):
		user_profile = UserProfile.objects.get(user_ptr=request.user)
		if request.method=="POST":
			data = request.POST
			pic = request.FILES.get("hall_pic")
			name=str(time.time())+pic.name
			path = os.path.join(settings.MEDIA_ROOT,name)
			f=open(path,"wb")
			for chunk in pic.chunks():
				f.write(chunk)
			f.close()
			hall = StudyHall(
					name=data.get("hall_name"), 
					area=data.get("hall_area"),
					pic=name,
					created_by=user_profile)
			hall.save()
		#studyhalls = StudyHall.objects.filter(created_by=user_profile,
		#	status=True)
		studyhalls = StudyHall.objects.filter(status=True)
		return render(request,"app1/studyhall.html",{"halls":studyhalls})
def view_hall_update(request,pk):
	hall = StudyHall.objects.get(pk=pk)
	if request.method=="POST":
		data = request.POST
		
		hall.name=data.get("name1")
		hall.area=data.get("area1")
		
		hall.save()
		return redirect(view_syudyhalls)

	return render(request,"app1/hall_update.html",{"data":hall})

def view_hall_delete(request, hall_id):
	hall_info = StudyHall.objects.get(pk=hall_id)
	if request.method=="POST":
		#hall_info.delete()
		hall_info.status=False
		hall_info.save()
		return redirect(view_syudyhalls)
	return render(request,"app1/hall_delete.html",{"hall":hall_info})
def view_reports(request):
	pass
def view_logout(request):
	if request.method=="POST":
		#request.session.clear()
		logout(request)
		return redirect(view_index)
	return render(request,"app1/logout.html")
def view_forgotpassword(request):
	pass