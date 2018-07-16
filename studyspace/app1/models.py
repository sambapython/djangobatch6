# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class StudyHall(models.Model):
	name = models.CharField(max_length=50)
	area = models.TextField(max_length=250)
	

