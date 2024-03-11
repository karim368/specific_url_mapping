from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def msd(request):
    return render(request,'msd.html')

def raina(request):
    return render(request,'raina.html')

def rahane(request):
    return HttpResponse('<center><h1>This is Ajinkya Rahane</center>')