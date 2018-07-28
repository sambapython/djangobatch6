# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework.response import Response
import json

from django.shortcuts import render
from api.models import StudyHall

# Create your views here.
class StudyHallView(APIView):
	def post(self, request):
		try:
			sh = StudyHall(**request.data)
			sh.save()
			return Response("study hall created successfully!!")
		except Exception as err:
			return Response(err.message)
	def put(self, request):

		return Response("hello world DRF put resp")
	def get(self, request):
		halls=StudyHall.objects.all()
		hals_det = map(lambda x: {"name":x.name,"area":x.area},halls)
		return Response(json.dumps(hals_det))
