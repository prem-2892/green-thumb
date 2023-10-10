from django.shortcuts import render
from django.http import HttpResponse
from .models import Program

# from .models import company


# class companies(ListView):
# model = Funding
# template_name = "GreenThumb/home.html"


def fetch(request):
    obj = Program.objects.all()
    context = {
        "data": obj,
    }
    return render(request, "index.html", context)
