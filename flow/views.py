from django.shortcuts import render, redirect
from .config import *
from .models import *
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.contrib.syndication.views import Feed


def home(request):
    posts = Post.objects.filter(post_status=True)
    paginator = Paginator(posts, MAXIMUM_OF_PAGE)
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
        post.post_views += 1
        post.save()
    except Post.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post})


def archives(request):
    try:
        post_list = Post.objects.filter(post_status=True)
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
            post_list = Post.objects.filter(post_title__icontains=s)
            if len(post_list) == 0:
                return render(request, 'archives.html', {'post_list': post_list,
                                                         'error': True})
            else:
                return render(request, 'archives.html', {'post_list': post_list,
                                                         'error': False})
    return redirect('/')


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


def post_meta(request, alias):
    try:
        meta_list = PostMeta.objects.filter(post_alias=alias)
    except Post.DoesNotExist:
        raise Http404
    return render(request, 'postmeta.html', {'meta_list': meta_list[0]})
