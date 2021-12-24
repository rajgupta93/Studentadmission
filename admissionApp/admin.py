from django.contrib import admin

from admissionApp.models import student
from .models import student
# Register your models here.
admin.site.register(student)