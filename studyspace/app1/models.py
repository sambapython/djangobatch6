# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.conf import  settings
# class MigrationModel(models.Model):
# 	def save(self, *args, **kwargs):
# 		for db in settings.DATABASES:
# 			kwargs.update({"using":db})
# 			if db=="default":
# 				df = super(MigrationModel,self).save(*args, **kwargs)
# 			else:
# 				super(MigrationModel,self).save(*args, **kwargs)
# 		return df
class model1(models.Model):
	name=models.CharField(max_length=250)
	def save(self, *args, **kwargs):
		for db in settings.DATABASES:
			kwargs.update({"using":db})
			if db=="default":
				df = super(model1,self).save(*args, **kwargs)
			else:
				super(model1,self).save(*args, **kwargs)
		return df
class model2(models.Model):
	name=models.CharField(max_length=250)
	def save(self, *args, **kwargs):
		for db in settings.DATABASES:
			kwargs.update({"using":db})
			if db=="default":
				df = super(model2,self).save(*args, **kwargs)
			else:
				super(model2,self).save(*args, **kwargs)
		return df
	



class Amazon(models.Model):
	name=models.CharField(max_length=250)
	database_name="default"
class VmWare(models.Model):
	name=models.CharField(max_length=250)
	database_name="default1"

class UserProfile(User):
	# it will create table in database: app1_userprofile
	# there is two columns role, user(onttoone relation with User model)
	roles = [("s","student"),("ss","studyspace")]
	up_name=models.CharField(max_length=250,default="")
	role = models.CharField(choices=roles, max_length=2,default="s")
	#user = models.OneToOneField(User)

	# def save(self, *args, **kwargs):
	# 	return UserProfile.objects.create(user_ptr=self.user_ptr,
	# 	 up_name=self.up_name)
	def __str__(self):
		return self.up_name
class UserProfile1(models.Model):
	# it will create table in database: app1_userprofile
	# there is two columns role, user(onttoone relation with User model)
	roles = [("s","student"),("ss","studyspace")]
	up_name=models.CharField(max_length=250,default="")
	role = models.CharField(choices=roles, max_length=2,default="s")
	user = models.OneToOneField(User)

	# def save(self, *args, **kwargs):
	# 	return UserProfile.objects.create(user_ptr=self.user_ptr,
	# 	 up_name=self.up_name)
	def __str__(self):
		return self.up_name


# class UserProfile(User):
# 	# it will create table in database: app1_userprofile
# 	# there is two columns role, user(onttoone relation with User model)
# 	roles = [("s","student"),("ss","studyspace")]
# 	role = models.CharField(choices=roles, max_length=2)

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
	pic = models.ImageField(blank=True, null=True)
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
class RequestTracker(models.Model):
	ip = models.CharField(max_length=250)
	path = models.CharField(max_length=2000)
	status = models.IntegerField(blank=True, null=True)










	

