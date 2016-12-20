from django.shortcuts import render
from django.shortcuts import HttpResponse
from mysite import models

# Create your views here.

def index(request):
    # return HttpResponse("Hello world!")
    if request.method == "POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        print (username,password)
        models.UserInfo.objects.create(user=username,pwd=password)
    user_list = models.UserInfo.objects.all()
    for i in user_list:
        print (i.user,i.pwd)
    return render(request,"index.html",{"data":user_list})