# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
	name=models.CharField(max_length=250)
	#name=models.CharField(max_length=250, primary_key=True)
	cost=models.IntegerField()

	class Meta:
		db_table="prouct"

