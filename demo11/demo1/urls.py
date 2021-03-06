"""demo1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/" , include("homeapp.urls")),
    path("compiler/" ,include("supercompiler.urls")),
    path("quizapp/" ,include("quizapp.urls")),
    path("aboutp/" ,include("about.urls")),
    path("contactp/" ,include("contact.urls")),
    path("userp/" ,include("users.urls")),
    path('login/' , user_view.login , name = 'login'),
    path('logout/' , auth.LogoutView.as_view(template_name = 'users/index.html') , name ='logout'),
    path('register/' , user_view.register , name = 'register'),
    

]
