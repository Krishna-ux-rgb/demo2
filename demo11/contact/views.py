from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def contact1(request):
    #return HttpResponse("<h1 style='text-align:center;color:cyan;'>Welcome To Videos Page!</h1>")
    return render(request , 'contact/contacthome.html')
# Create your views here.
