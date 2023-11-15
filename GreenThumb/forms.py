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

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Submit"))

        self.helper.layout = Layout(
            Div(
                "company_name",
                "contact_info",
                "postal_code",
                css_class="flex flex-col md:flex-row gap-4 md:items-end",
            ),
            Div(
                "employee_count",
                "annual_electricity_budget",
                "company_sector",
                css_class="flex flex-col md:flex-row gap-4 md:items-end",
            ),
            Div(
                "annual_natural_gas_budget",
                css_class="flex gap-4 items-end",
            ),
            # Add more Div elements as needed
        )
