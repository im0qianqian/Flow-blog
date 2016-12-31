from django.shortcuts import render, redirect
from .models import *
from flow.config import *
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.syndication.views import Feed


def home(request):
    # 选出所有未隐藏的文章并同时链接查询出其作者与分类
    posts = Post.objects.filter(status=True).select_related('author', 'category')
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
    # 链接用户表与分类表多表查询
    post = Post.objects.filter(id=id, status=True).select_related('author', 'category')
    if len(post) == 0:
        raise Http404
    else:
        post = post[0]
        post.views += 1
        post.save()
        return render(request, 'post.html', {'post': post})


def archives(request):
    post_list = Post.objects.filter(status=True)
    return render(request, 'archives.html', {'post_list': post_list})


def search_tag(request, tag):
    # 与Tag多对多链接 结果集放在res中
    post_list = Post.objects.prefetch_related('tag')
    res = []
    for post in post_list:
        if post.tag.filter(title=tag):
            res.append(post)
    return render(request, 'tag.html', {'post_list': res})


def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request, 'home.html')
        else:
            post_list = Post.objects.filter(title__icontains=s)
            return render(request, 'archives.html', {'post_list': post_list})
    return redirect('/')


class RSSFeed(Feed):
    title = "RSS feed - article"
    link = "feed/posts/"
    description = "RSS feed - blog posts"

    def items(self):
        return Post.objects.order_by('-created')

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.created

    def item_description(self, item):
        return item.excerpt


# 获取当前所创建的所有页面
def get_page():
    return Page.objects.only('title', 'alias',)


def post_meta(request, alias):
    post = Page.objects.filter(alias=alias)
    if len(post) == 0:
        raise Http404
    else:
        post[0].id = -post[0].id
        return render(request, 'page.html', {'post': post[0]})


def links(request):
    links = Link.objects.all()
    return render(request, 'links.html', {'links': links})
