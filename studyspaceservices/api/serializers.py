from rest_framework import serializers
from api.models import Expenses, StudyHall
class ExpSerializer(serializers.ModelSerializer):
	def validate_studyhall(self, hall):
		
		try:
			hall = StudyHall.objects.get(pk=hall.id)
			return self.data
		except Exception as err:
			return self._errors


	class Meta:
		model=Expenses
		fields =("id","studyhall","date","desc","value","name")
class ExpSerializerGet(serializers.ModelSerializer):
	class Meta:
		model=Expenses
		fields =("id","studyhall","date","desc","value","name")

