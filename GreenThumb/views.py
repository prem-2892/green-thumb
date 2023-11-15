# views.py
from django.http import HttpResponse
from django.forms import modelformset_factory
from .models import Company, Program
from .forms import CompanyForm
from django.shortcuts import render
from django.db.models import Q


CompanyFormSet = modelformset_factory(Company, form=CompanyForm, extra=1)


def index(request):
    suitable_programs = []
    if request.method == "POST":
        formset = CompanyFormSet(request.POST)
        if formset.is_valid():
            # pass
            formset.save()

            suitable_programs = Program.objects.filter(
                Q(
                    eligible_employee_count__count__contains=formset.cleaned_data[0][
                        "employee_count"
                    ]
                )
                | Q(eligible_employee_count=None),
                Q(
                    eligible_annual_electricity_budget__budget__contains=formset.cleaned_data[
                        0
                    ][
                        "annual_electricity_budget"
                    ]
                )
                | Q(eligible_annual_electricity_budget=None),
                Q(
                    eligible_company_sector__name__contains=formset.cleaned_data[0][
                        "company_sector"
                    ]
                )
                | Q(eligible_company_sector=None),
                Q(
                    eligible_annual_natural_gas_budget__budget__contains=formset.cleaned_data[
                        0
                    ][
                        "annual_natural_gas_budget"
                    ]
                )
                | Q(eligible_annual_natural_gas_budget=None),
            )

    else:
        formset = CompanyFormSet(queryset=Company.objects.none())

    return render(
        request,
        "home1.html",
        {
            "formset": formset,
            "suitable_programs": suitable_programs,
            "form": CompanyForm,
        },
    )
