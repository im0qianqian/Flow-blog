from django.shortcuts import render
from django.shortcuts import HttpResponse
from mysite import models

# Create your views here.

def index(request):
    # return HttpResponse(a+"Hello world!"+b)
    user_list = range(0,20)
    return render(request,"index.html",{"user_list":user_list})