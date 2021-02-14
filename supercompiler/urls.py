from django.urls import path
from  . import views




urlpatterns = [
    path('' , views.compilerapp),
    path('executeCode/' , views.executeTheCode),
]