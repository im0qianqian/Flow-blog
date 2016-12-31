from django.shortcuts import render, redirect
from .models import *
from flow.config import *
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.syndication.views import Feed


def home(request):
    posts = Post.objects.filter(status=True)
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
        post.views += 1
        post.save()
    except Post.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post})


def archives(request):
    try:
        post_list = Post.objects.filter(status=True)
    except Post.DoesNotExist:
        raise Http404
    return render(request, 'archives.html', {'post_list': post_list,
                                             'error': False})


def search_tag(request, tag):
    try:
        post_list = Post.objects.filter(tag=tag)
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


class RSSFeed(Feed):
    title = "RSS feed - article"
    link = "feeds/posts/"
    description = "RSS feed - blog posts"

    def items(self):
        return Post.objects.order_by('-created')

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.created

    def item_description(self, item):
        return item.content


def post_meta(request, alias):
    try:
        post = Page.objects.filter(alias=alias)
    except Post.DoesNotExist:
        raise Http404
    if len(post) == 0:
        return render(request, 'post.html', {'error': True})
    else:
        post[0].id = -post[0].id
        return render(request, 'post.html', {'post': post[0], 'error': False})


def links(request):
    links = Link.objects.all()
    return render(request, 'links.html', {'links': links})
