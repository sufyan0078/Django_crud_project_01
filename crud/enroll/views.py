from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.
#This method is used to add and show data
def add_show(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
          #  fm.save()it is also used to save data in DB but not a good way
          nm = fm.cleaned_data["name"]
          em = fm.cleaned_data["email"]
          pw = fm.cleaned_data["password"]
          reg = User(name=nm,email=em,password=pw)
          reg.save()
          fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request,"enroll/addandshow.html",{"form":fm,"stu":stud})
def update_data(request,id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save() 
        fm = StudentRegistration()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request,"enroll/updatestudent.html",{"form":fm})
#This method will delete data
def del_data(request,id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect("/")

