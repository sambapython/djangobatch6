from django.forms import ModelForm
from .models import Enquiry, Expenses
from django.forms.widgets import DateInput

class ExpensesForm(ModelForm):
	class Meta:
		model=Expenses
		fields = "__all__"
	def __init__(self, *args, **kwargs):
		super(ModelForm, self).__init__(*args, **kwargs)
		for field,field_inst in self.fields.items():
			if field=="date":
				field_inst.widget.attrs.update({"id":"datefield"})
			field_inst.widget.attrs.update({"class":"form-control"})
		


