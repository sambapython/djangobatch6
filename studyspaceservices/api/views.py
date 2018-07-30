# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json

from django.shortcuts import render
from api.models import StudyHall
def validate_name(name):
	if isinstance(name,str):
		return name.isalpha()
	else:
		return False

# Create your views here.
class StudyHallView(APIView):
	def post(self, request):
		try:
			data = request.data
			if "name" in data and "area" in data:
				if not validate_name(data.get("name")):
					return Response("Validation error",
						status=status.HTTP_406_NOT_ACCEPTABLE)
				sh = StudyHall(**request.data)
				sh.save()
				return Response("study hall created successfully!!")
			else:
				return Response("name, area params are required",
					status=status.HTTP_400_BAD_REQUEST)
		except Exception as err:
			return Response(err.message, 
				status=status.HTTP_500_INTERNAL_SERVER_ERROR)
	def get(self, request):
		halls=StudyHall.objects.all()
		hals_det = map(lambda x: {"name":x.name,"area":x.area},halls)
		return Response(json.dumps(hals_det))

class StudyHallDetailView(APIView):
	def put(self, request, pk):
		#import pdb; pdb.set_trace()

		try:
			if "name" in data or "area" in data:
				if not validate_name(data.get("name")):
					return Response("Validation error",
						status=status.HTTP_406_NOT_ACCEPTABLE)
				hall = StudyHall.objects.get(pk=pk)
				data = request.data
				hall.name=data.get("name", hall.name)
				hall.area = data.get("area",hall.area)
				hall.save()
				return Response("Success fully updated")
			else:
				return Response("name, area params are required",
					status=status.HTTP_400_BAD_REQUEST)
		except Exception as err:
			return Response("error in the updation",
				status=status.HTTP_404_NOT_FOUND)
	def get(self, request, pk):
		#import pdb; pdb.set_trace()
		try:
			hall = StudyHall.objects.get(pk=pk)
			data = {"name":hall.name,"area":hall.area}
			return Response(data)
		except Exception as err:
			return Response("not found",
				status=status.HTTP_404_NOT_FOUND)
	def delete(self, request, pk):
		#import pdb; pdb.set_trace()
		try:
			hall = StudyHall.objects.get(pk=pk)
			hall.delete()
			return Response("successfully deleted")
		except Exception as err:
			return Response("not found",
				status=status.HTTP_404_NOT_FOUND)

