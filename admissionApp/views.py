from django.http.response import HttpResponse
from django.shortcuts import render
from .models import student
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.models import User , auth
# Create your views here.

def merit(request):
    merit=student.objects.all()
    stud={
        "data":merit
    }
    return render(request,"merit.html",stud)
def merit_id(request,student_id):
    stud_details=student.objects.get(id=student_id)
    stud={
        "data":stud_details
    }
    return render(request,"studentdetails.html",stud) 

def application(request):

    # if request.user.is_authenticated:
        stud_details=student.objects.all
        stud={
        "data":stud_details
        }
        return render(request,"application.html",stud)
    # else:
    #     return render(request,"application.html") 

def adminlogin(request):

    if request.user.is_authenticated:
        return application(request)
    else:
        if request.method == 'POST':
            username=request.POST['email']
            password=request.POST['password']
            user =auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return application(request)
            else:
                print('email',username)
                print('password',password)
                render(request,"adminlogin.html")
        
        else:
            return render(request,"adminlogin.html")

def studentregistration(request):

    if request.method == 'POST':
        firstname=request.POST['fname']
        middlename=request.POST['mname']
        lastname=request.POST['lname']
        # date=request.POST['dob']
        # age=request.POST['age']
        # gender=request.POST['gender']
        email=request.POST['email']
        ftname=request.POST['ftname']
        mtname=request.POST['mtname']
        mobile=request.POST['mobile']
        tenthBoard=request.POST['tenthBoard']
        tenthSchool=request.POST['tenthSchool']
        tenthPercent=request.POST['tenthPercent']
        twelveBoard=request.POST['twelveBoard']
        twelveSchool=request.POST['twelveSchool']
        twelvePercent=request.POST['twelvePercent']
        print("name",firstname)
        register=student(firstName=firstname,middleName=middlename,lastName=lastname,motherName=mtname,fatherName=ftname
        ,mobile=mobile,mailId=email,tenthBoard=tenthBoard,tenthSchool=tenthSchool,tenthPercent=tenthPercent,twelveBoard=twelveBoard,twelvePercent=tenthPercent
        ,twelveSchool=twelveSchool)
        register.save()        
    else:
        details=student()    
    return render(request,"studentregistration.html")

