from django.shortcuts import render
from .models import Question
# Create your views here.
def quizhome(request):
    questions = Question.objects.all()
    return render(request , "quizapp/quizhome.html" , {'Questions' : questions}) 

