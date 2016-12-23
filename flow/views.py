from django.shortcuts import render, redirect
from .models import *
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    posts = Post.objects.all()  # 获取全部的Article对象
    paginator = Paginator(posts, 2)  # 每页显示两个
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'home.html', {'post_list': post_list})


def detail(request, id):
    try:
        post = Post.objects.get(id=str(id))
    except Post.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post})


def archives(request):
    try:
        post_list = Post.objects.all()
    except Post.DoesNotExist:
        raise Http404
    return render(request, 'archives.html', {'post_list': post_list,
                                             'error': False})


def search_tag(request, tag):
    try:
        post_list = Post.objects.filter(post_tag=tag)
    except Post.DoesNotExist:
        raise Http404
    return render(request, 'tag.html', {'post_list': post_list})


def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request, 'home.html')
        else:
            post_list = Post.objects.filter(title__icontains=s)
            if len(post_list) == 0:
                return render(request, 'archives.html', {'post_list': post_list,
                                                         'error': True})
            else:
                return render(request, 'archives.html', {'post_list': post_list,
                                                         'error': False})
    return redirect('/')


from django.contrib.syndication.views import Feed  # 注意加入import语句


class RSSFeed(Feed):
    title = "RSS feed - article"
    link = "feeds/posts/"
    description = "RSS feed - blog posts"

    def items(self):
        return Post.objects.order_by('-post_date')

    def item_title(self, item):
        return item.post_title

    def item_pubdate(self, item):
        return item.post_date

    def item_description(self, item):
        return item.post_content
