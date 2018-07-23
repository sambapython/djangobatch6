# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from app1.models import StudyHall, Expenses, Enquiry, Course, Student,\
 Expenses, UserProfile
from django.contrib.auth import authenticate, login, logout

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
def view_syudyhalls(request):
	if "user" in request.session:
		if request.method=="POST":
			data = request.POST
			hall = StudyHall(name=data.get("hall_name"), 
					area=data.get("hall_area"))
			hall.save()
		studyhalls = StudyHall.objects.all()
		return render(request,"app1/studyhall.html",{"halls":studyhalls})
	else:
		return redirect(view_index)
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
		hall_info.delete()
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