"""
URL configuration for turf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from Application import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="Home"),
    path('Login/',views.loginpage,name="login"),
    path('Register/',views.registerpage,name="Register"),
    path('Contact/',views.contactpage,name="Contact"),
    path('User/<int:id>/<str:uname>/',views.userdetails,name='Userdetails'),
    path('Slotbooking/<int:id>/',views.slotbooking,name="allsports"),
    path('Deletslot/<int:id>/<str:date>/<str:time>/<str:sport>/<str:mail>/',views.deleteslot,name="Deleteslot"),   
    path('Cricket/<int:id>/',views.cricketview,name="Cricket"),
    path('Cricketslotbook/',views.Cricketbook,name="Cricketbook"),
    path('Football/<int:id>/',views.footballview,name="Football"),
    path('Footballbook/',views.footballbook,name="Footballbook"),
    path('Basketball/<int:id>/',views.basketballview,name="Basketball"),
    path('Basketbook/',views.basketballbook,name="Basketballbook"),
    path('Handball/<int:id>/',views.handballview,name="Handball"),
    path('Handball/',views.handballbook,name="Handballbook"),
    path('volleyball/<int:id>/',views.handballview,name="Volleyball"),
    path('volleyballslotbook/',views.handballbook,name="Volleyballbook"),
    path('kabaddi/<int:id>/',views.handballview,name="Kabaddi"),
    path('kabaddislotbook/',views.handballbook,name="Kabaddibook"),
    
]
