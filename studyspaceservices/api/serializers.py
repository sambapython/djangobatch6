from rest_framework import serializers
from api.models import Expenses, StudyHall
class ExpSerializer(serializers.ModelSerializer):
	def validate_studyhall(self, value):
		
		try:
			hall = StudyHall.objects.get(pk=value.id)
			return value
		except Exception as err:
			return serializers.ValidationError("studyhall not found")
	def validate_name(self, value):
		if not value.isalpha():
			return serializers.ValidationError("name should be alpha numeric")
		return value


	class Meta:
		model=Expenses
		fields =("id","studyhall","date","desc","value","name")
class ExpSerializerGet(serializers.ModelSerializer):
	class Meta:
		model=Expenses
		fields =("id","studyhall","date","desc","value","name")

