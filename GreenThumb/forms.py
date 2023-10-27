from django.forms import ModelForm
from .models import Company

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'  # You can specify which fields you want to include in the form
