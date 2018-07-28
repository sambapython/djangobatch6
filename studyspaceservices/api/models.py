# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
class UserProfile(User):
	# it will create table in database: app1_userprofile
	# there is two columns role, user(onttoone relation with User model)
	roles = [("s","student"),("ss","studyspace")]
	role = models.CharField(choices=roles, max_length=2)


class UserProfile(User):
	# it will create table in database: app1_userprofile
	# there is two columns role, user(onttoone relation with User model)
	roles = [("s","student"),("ss","studyspace")]
	role = models.CharField(choices=roles, max_length=2)

class NameModel(models.Model):
	# abstract model
	# it wont create table in the background
	status = models.BooleanField(default=True)
	name = models.CharField(max_length=250, unique=True)
	created_by = models.ForeignKey(UserProfile, blank=True, null=True)
	created_date = models.DateTimeField(auto_now_add=True)

	class Meta:
		abstract=True


# Create your models here.
class StudyHall(NameModel):
	#name = models.CharField(max_length=50)
	area = models.TextField(max_length=250)
	pic = models.ImageField()
	
	def __str__(self):
		return "%s|%s"%(self.name, self.area)

class Expenses(NameModel):
	studyhall = models.ForeignKey(StudyHall)
	date = models.DateTimeField()
	#name=models.CharField(max_length=250)
	desc = models.TextField(max_length=250)
	value= models.IntegerField()

	def __str__(self):
		return "%s,%s,%s,%s"%(self.studyhall, 
			self.date, 
			self.value,
		 	self.desc)

class Course(NameModel):
	#ame = models.CharField(max_length=250)

	def __str__(self):
		return self.name
class Student(NameModel):
	#name=models.CharField(max_length=250)
	address = models.TextField(max_length=250)
	phone = models.CharField(max_length=10)
	email = models.CharField(max_length=250)

	def __str__(self):
		return self.name


class Enquiry(NameModel):
	#name = models.CharField(max_length=250)
	course = models.ForeignKey(Course)
	student = models.ForeignKey(Student)
	def __str__(self):
		return "%s,%s,%s"%(self.name,self.student,self.course)









	

