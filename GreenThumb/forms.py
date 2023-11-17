from django.forms import ModelForm
from .models import Company
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = (
            "__all__"  # You can specify which fields you want to include in the form
        )
