# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
import json
from rest_framework.decorators import authentication_classes,\
permission_classes

from django.shortcuts import render
from api.models import StudyHall, Expenses
from serializers import ExpSerializer, ExpSerializerGet,\
StudyHallSerializer
class ExpensesView(APIView):
	#permission_classes = (permissions.IsAuthenticated,)
	def get(self, request):
		data = Expenses.objects.all()
		expser = ExpSerializerGet(data, many=True)
		return Response(expser.data)
	def post(self, request):
		try:		
			exp_ser = ExpSerializer(data=request.data)
			if exp_ser.is_valid():
				exp_ser.save()
				return Response("Expense created successfully")
			else:
				return Response(exp_ser._errors,
					status=status.HTTP_400_BAD_REQUEST)
		except Exception as err:
			return Response(err.message,
				status=status.HTTP_500_INTERNAL_SERVER_ERROR)
	# def post(self, request):
	# 	try:

	# 		hall = StudyHall.objects.get(pk=request.data.get("studyhall"))
	# 		request.data.update({"studyhall":hall})
	# 		exp = Expenses(**request.data)
	# 		exp.save()
	# 		return Response("Expense created successfully")
	# 	except Exception as err:
	# 		return Response(err.message,
	# 			status=status.HTTP_500_INTERNAL_SERVER_ERROR)
def validate_name(name):
	if isinstance(name,str):
		return name.isalpha()
	else:
		return False
@authentication_classes([])
@permission_classes([])
class StudyHallView(APIView):
	# def post(self, request):
	# 	try:
	# 		data = request.data
	# 		#sh = StudyHall(**request.data)
	# 		#sh.save()
	# 		studyhallser = StudyHallSerializer(data=data)
	# 		if studyhallser.is_valid():
	# 			studyhallser.save()
	# 		else:
	# 			return Response(studyhallser._errors)
	# 		return Response("study hall created successfully!!")
	# 	except Exception as err:
	# 		return Response(err.message, 
	# 			status=status.HTTP_500_INTERNAL_SERVER_ERROR)
	def post(self, request):
		try:
			data = request.data
			studyhallser = StudyHallSerializer(data=data)
			if studyhallser.is_valid():
				studyhallser.save()
				return Response("studyhall created successfully")
			else:
				return Response(studyhallser._errors,
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

