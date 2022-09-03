from ctypes import DllGetClassObject
from django.shortcuts import render
from app1.forms import  Practice, StudentF, UserInfoForm, studentInfo, studentform
from app1.models import P, Student, Student1

# Create your views here.

def login(request):
    context={'data':'This is login page'}
    return render(request,'app1/app1.html',context)

def home(request):
    form = studentform()
    if request.method =='POST':
        form = studentform(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Invalid Data")
        form = studentform()   
    return render(request,'app1/home.html',{'form':form})

def app1(request):
    form = UserInfoForm()
    if request.method =='POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Invalid Data")
        form = UserInfoForm()   
    return render(request,'app1/home.html',{'form':form})

def customers(request):
    form = StudentF()
    if request.method == "POST":
        form = StudentF(request.POST)
        if form.is_valid():
            sid=form.cleaned_data.get('sid')
            sname=form.cleaned_data.get('sname')
            email=form.cleaned_data.get('email')
            contact=form.cleaned_data.get('contact')
            studentdata=Student(sid=sid,sname=sname,email=email,contact=contact)
            studentdata.save()
        else:
            print("invalid data")
        form=StudentF()
    return render(request,'app1/home.html',{'form':form})

def products(request):
    form = studentInfo()
    if request.method == "POST":
        form = studentInfo(request.POST)
        if form.is_valid():
            sid=form.cleaned_data['sid']
            sname=form.cleaned_data['sname']
            fee=form.cleaned_data['fee']
            doj=form.cleaned_data['doj']
            students=Student1(sid=sid,sname=sname,fee=fee,doj=doj)
            students.save()
        else:
            print("invalid data")
        form=studentInfo()
    return render(request,'app1/home.html',{'form':form})

def orders(request):
    form = Practice()
    if request.method == "POST":
        form = Practice(request.POST)
        if form.is_valid():
            sid=form.cleaned_data['sid']
            sname=form.cleaned_data['sname']
            courses=form.cleaned_data['courses']
            students=P(sid=sid,sname=sname,courses=courses)
            students.save()
        else:
            print("invalid data")
        form=Practice()
    return render(request,'app1/home.html',{'form':form})

