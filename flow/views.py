from django.shortcuts import render
from .models import *
from django.http import Http404


# Create your views here.

def home(request):
    post_list = Post.objects.all()
    print(post_list)
    return render(request, 'home.html', {'post_list': post_list})


def archives(request, id):
    try:
        post = Post.objects.get(id=str(id))
    except Post.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post})
