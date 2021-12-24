
from django.contrib import admin
from django.urls import path,include
from admissionApp import views
urlpatterns = [
    path('', views.merit,name='merit'),
    path('merit/<student_id>/',views.merit_id),
    path('application',views.application),
    path('adminlogin',views.adminlogin),
    path('studentregistration',views.studentregistration)
]
