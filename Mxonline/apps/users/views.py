#coding=utf-8

from django.shortcuts import render

# Create your views here.

def LoginView(request):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        return render(request,'login.html',{})


