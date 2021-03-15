from django.http import HttpResponse
from django.shortcuts import render
from .models import Hereglegch

def index(request):
    return HttpResponse("jnjfndkjb")

def home(request):
    data=Hereglegch.objects.all()
    return render(request,'index.html',{'ddd':data})