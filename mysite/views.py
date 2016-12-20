from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("Hello world!")
    if request.method == "POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        print (username,password)
        return render(request,"index.html")
    return render(request,"index.html")