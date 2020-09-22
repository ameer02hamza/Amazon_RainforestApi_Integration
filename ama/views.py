from django.shortcuts import render
from api import api_ama, test
from  django import template
# Create your views here.

def index(request):
    data = api_ama.apic['category_results']
    print(data[2])

    return render(request, "index.html", {"data":data})
