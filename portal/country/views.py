from django.shortcuts import render
from .models import country

# Create your views here.

def index(request):
    coun = country.objects.all
    return render(request, "country.html", context={"country":coun})