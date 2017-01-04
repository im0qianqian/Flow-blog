"""Pyblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from flow import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home),
    url(r'^detail/(?P<id>\d+).html$', views.detail, name='detail'),
    url(r'^links$', views.links, name='links'),
    url(r'^tag/(?P<tag>\w+)/?$', views.search_tag, name='search_tag'),
    url(r'^categories/?$', views.categories, name='categories'),
    url(r'^category/(?P<category>\w+)/?$', views.category, name='category'),
    url(r'^search/$', views.blog_search, name='search'),
    url(r'^feed$', views.RSSFeed(), name="RSS"),
    url(r'^(?P<alias>\w+)$', views.post_meta, name="post_meta"),
]
