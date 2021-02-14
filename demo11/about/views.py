from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def about1(request):
   # ("<h1 style='text-align:center;color:cyan;'>Welcome To about Page!</h1>")
    return render(request , 'about/abouthome.html')

# Create your views here.
