# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from app1.models import Course, StudyHall, Student, Enquiry,\
Expenses,UserProfile1

# Register your models here.
admin.site.register(Course)
admin.site.register(StudyHall)
admin.site.register(Student)
admin.site.register(Enquiry)
admin.site.register(Expenses)
admin.site.register(UserProfile1)
