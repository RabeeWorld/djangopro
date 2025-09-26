from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
# Create your views here.

#
# def home(request):
#     return HttpResponse("<h1><font color='red'>Hello students</font></h1>")

def home(request):
    return render(request,"index.html")

def add_student(request):
    nm=request.POST['name']
    rlno=request.POST['rno']
    addr=request.POST['address']
    mno=request.POST['mbno']

    try:
        st=Student(Name=nm,Roll_no=rlno,Address=addr,Mobile_no=mno)
        st.save()
        return render(request,"index.html",{"msg1":"Student record created"})
    except Exception as E:
        return render(request,"index.html",{"msg1":"student not created"})