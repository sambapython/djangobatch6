# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from app1.models import StudyHall, Expenses, Enquiry, Course, Student, Expenses

# Create your views here.
def view_index(request):
	if request.method=="POST":
		data = request.POST
		if data.get("enquiry"):
			course_inst = Course.objects.get(pk=data.get("enq_course"))
			stdudent_inst = Student.objects.get(pk=data.get("enq_student"))
			enq = Enquiry(
				name = data.get("enq_name"),
				student = stdudent_inst,
				course = course_inst
				)
			enq.save()
		elif data.get("expense"):
			studyhall_inst = StudyHall.objects.get(pk=data.get("exp_studyhall"))
			exp = Expenses(
				studyhall = studyhall_inst,
				date = data.get("exp_date"),
				name = data.get("exp_name"),
				desc = data.get("exp_desc"),
				value = data.get("exp_value"),
				)
			exp.save()
		else:
			hall = StudyHall(name=data.get("hall_name"), 
				area=data.get("hall_area"))
			hall.save()
	studyhalls = StudyHall.objects.all()
	expenses = Expenses.objects.all()
	enquiries = Enquiry.objects.all()
	courses = Course.objects.all()
	students = Student.objects.all()
	return render(request,"app1/index.html",{
		"halls": studyhalls,
		"exps": expenses,
		"enqs": enquiries,
		"students": students,
		"courses": courses 
		})
def view_syudyhalls(request):
	studyhalls = StudyHall.objects.all()
	return render(request,"app1/index.html",{"studyhalls":studyhalls})
def view_hall_update(request,pk):
	hall = StudyHall.objects.get(pk=pk)
	if request.method=="POST":
		data = request.POST
		hall.name=data.get("name1")
		hall.area=data.get("area1")
		hall.save()
		return redirect(view_index)

	return render(request,"app1/hall_update.html",{"data":hall})

def view_hall_delete(request, hall_id):
	hall_info = StudyHall.objects.get(pk=hall_id)
	if request.method=="POST":
		hall_info.delete()
		return redirect(view_index)
	return render(request,"app1/hall_delete.html",{"hall":hall_info})