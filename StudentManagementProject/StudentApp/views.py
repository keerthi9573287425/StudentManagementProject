from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.views.decorators.cache import cache_control, never_cache

from StudentApp.models import City, Course, Student
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache

def reg_fun(request):
    return render(request,'register.html',{'data':''})

@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def regdata_fun(request):
    user_name = request.POST['txtUserName']
    user_email = request.POST['txtEmail']
    user_pswd = request.POST['txtPswd']


    if User.objects.filter(Q(username=user_name) | Q(email=user_email)).exists():
     return render(request,'register.html',{'data':'username,email and password is already exists'})
    else:
        u1=User.objects.create_superuser(username=user_name,email=user_email,password=user_pswd)
        u1.save()
        return redirect('log')


@cache_control(no_cache=True, revalidate=True, nostore=True)
@never_cache
def log_fun(request):
    return render(request,'login.html',{'data':''})

@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def log_read(request):
    User_Name = request.POST['txtUserName']
    User_Pswd = request.POST['txtPswd']
    user1 = authenticate(username=User_Name,password=User_Pswd)
    if user1 is not None:
        if user1.is_superuser:
            login(request,user1)
            return redirect('home')
        else:
            return render(request,'login.html',{'data':'User is not superuser'})
    else:
        return render(request,'login.html',{'data':'enter proper username and password'})

@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def home_fun(request):
    return render(request,'home.html')

@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def addstudent_fun(request):
    city= City.objects.all()
    course= Course.objects.all()
    return render(request,'addstudent.html',{'City_Data' : city, 'Course_Data' :course})

@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def readdata_fun(request):
    s1 = Student()
    s1.stud_Name = request.POST['txtName']
    s1.stud_Age = request.POST['txtAge']
    s1.stud_Phno = request.POST['txtPhno']
    s1.stud_City = City.objects.get(City_Name = request.POST['ddlCity'])
    s1.stud_Course = Course.objects.get(Course_Name = request.POST['ddlCourse'])
    s1.save()
    return redirect('add')

@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def display_fun(request):
    s1=Student.objects.all()
    return render(request,'display.html',{'data':s1})

@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def update_fun(request,id):
    s1=Student.objects.get(id=id)
    city = City.objects.all()
    course = Course.objects.all()
    if request.method == 'POST':
        s1.stud_Name = request.POST['txtName']
        s1.stud_Age = request.POST['txtAge']
        s1.stud_Phno = request.POST['txtPhno']
        s1.stud_City = City.objects.get(City_Name=request.POST['ddlCity'])
        s1.stud_Course = Course.objects.get(Course_Name=request.POST['ddlCourse'])
        s1.save()
        return redirect('display')

    return render(request,'update.html',{'data':s1,'City_Data':city,'Course_Data':course})
@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def delete_fun(request,id):
    s1=Student.objects.get(id=id)
    s1.delete()
    return redirect('display')

@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def log_out_fun(request):
    logout(request)
    return redirect('log')