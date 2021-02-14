from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, "homeapp/homepage.html" ,{'check':1000})
