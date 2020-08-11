"""AMIS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from amisapp1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('registration/',views.registration,name='registration'),
    path('user_login',views.user_login,name='login'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('patientDashboard/',views.patientDashboard,name='patientDashboard'),
    path('doctorDashboard/',views.doctorDashboard,name='doctorDashboard'),
    path('labDashboard/',views.labDashboard,name='labDashboard'),
    path('pharmacistDashboard/',views.pharmacistDashboard,name='pharmacistDashboard'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('doctors/',views.doctors,name='doctors'),
    path('check/',views.check,name='check'),
    path('service/',views.service,name='service'),
    path('profile/',views.profile,name='profile'),
    path('appointment/',views.appointment,name='appointment'),
    path('covid/',views.covid,name='covid'),
    path('patientAppointmentBook/',views.patientAppointmentBook,name='patientAppointmentBook'),
    path('checkuplist/', views.checkuplist, name='checkuplist'),
    path('appointmentlist/', views.appointmentlist, name='appointmentlist'),
    path('paymentstatus/', views.paymentstatus, name='paymentstatus'),
    path('labreport/', views.labreport, name='labreport'),
    path('notification/', views.notification, name='notification'),
    path('learn/', views.learn, name='learn'),
    path('expert/', views.expert, name='expert'),
    path('shop/', views.shop, name='shop'),
    path('tech/', views.tech, name='tech'),
    path('formservice', views.formservice, name='formservice')


]

