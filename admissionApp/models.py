from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.
class student(models.Model):
    firstName=models.CharField(max_length=40)
    middleName=models.CharField(max_length=40)
    lastName=models.CharField(max_length=40)
    motherName=models.CharField(max_length=40)
    fatherName=models.CharField(max_length=40)
    id = models.AutoField(primary_key=True)
    mobile=models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)])
    # age=models.IntegerField()
    mailId=models.CharField(max_length=40)
    # dob=models.DateField(default='12/10/2001')
    # gender=models.CharField(max_length=1)
    # address=models.CharField(max_length=100)
    # caste=models.CharField(max_length=10)
    # selected=models.IntegerField(default=2)
    # tenthmarks=models.IntegerField(default=0)
    tenthSchool=models.CharField(max_length=100,default="")
    tenthPercent=models.CharField(max_length=100,default="")
    tenthBoard=models.CharField(max_length=100,default="")
    twelvePercent=models.IntegerField(default=0)
    twelveSchool=models.CharField(max_length=100,default="")
    # twelfthpassingyear=models.CharField(max_length=100,default="")
    twelveBoard=models.CharField(max_length=100,default="")
    