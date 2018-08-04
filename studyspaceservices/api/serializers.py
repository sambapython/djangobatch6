from rest_framework import serializers
from api.models import Expenses, StudyHall
class StudyHallSerializer(serializers.ModelSerializer):
	class Meta:
		model = StudyHall
		#fields="__all__"
		fields=("name","area")

	def validate_name(self, value):
		if value.isalpha():
			return value 
		raise serializers.ValidationError(
			"name should contains only alphabets")

	def validate_area(self, value):
		if value.isalnum():
			return value 
		raise serializers.ValidationError(
			"area should contains only alpha nummeric")

class ExpSerializer(serializers.ModelSerializer):
	# def validate_studyhall(self, hall):
		
	# 	try:
	# 		hall = StudyHall.objects.get(pk=hall.id)
	# 		return self.data
	# 	except Exception as err:
	# 		return self._errors


	class Meta:
		model=Expenses
		fields =("id","studyhall","date","desc","value","name")
class ExpSerializerGet(serializers.ModelSerializer):
	class Meta:
		model=Expenses
		fields =("id","studyhall","date","desc","value","name")

