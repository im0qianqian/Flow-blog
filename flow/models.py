from django.db import models
from flow.config import *
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


# class User(models.Model):
#     user_nickname = models.CharField(max_length=30,blank=True)
#     user_login = models.CharField(max_length=30,unique=True)
#     user_pass = models.CharField(max_length=40)
#     user_email = models.EmailField(unique=True,blank=True)
#     user_url = models.URLField(max_length=50,blank=True)
#     user_registered = models.DateTimeField(auto_now_add=True)
#     key_grade = models.IntegerField(default=GRADE_KEY['contributors'])
#
#     def __str__(self):
#         return self.user_nickname


class PostMeta(models.Model):
    title = models.CharField('Title', max_length=80, blank=True)
    content = models.TextField('Content', blank=True)
    alias = models.CharField('Alias', max_length=80, blank=True, unique=True, default=title)
    datetime = models.DateTimeField('Created time', auto_now_add=True, editable=True)
    modified = models.DateTimeField('Last Modified', auto_now=True, editable=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    STATUS_CHOICES = (
        (True, 'Public'),
        (False, 'Hide')
    )
    author = models.ForeignKey(User)
    datetime = models.DateTimeField('Created Time', auto_now_add=True, editable=True)
    modified = models.DateTimeField('Last Modified', auto_now=True, editable=True)
    title = models.CharField('Title', max_length=80, blank=True)
    content = models.TextField('Content', blank=True)
    excerpt = models.TextField('Excerpt', blank=True)
    status = models.BooleanField('Article status', default=False, choices=STATUS_CHOICES)
    password = models.CharField('Password', max_length=80, blank=True)
    alias = models.CharField('Alias', max_length=80, blank=True, unique=True, default=title)
    category = models.ForeignKey('Category')
    tag = models.ManyToManyField('Tag', blank=True)
    views = models.PositiveIntegerField('Pageviews', editable=False, default=0)
    image = models.URLField('Image', blank=True)

    def __str__(self):
        return self.title

    # Get the archives url. Maybe for duoshuo.
    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id': self.id})
        return "http://127.0.0.1:8000/%s" % path

    class Meta:
        ordering = ['-datetime']


class Link(models.Model):
    title = models.CharField('Title', max_length=30, blank=True)
    url = models.URLField('Url', unique=True)
    description = models.TextField('Description', blank=True)
    image = models.URLField('Image', blank=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField('Title', max_length=30)
    alias = models.CharField('Alias', max_length=30, blank=True, unique=True, default=title)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post_id = models.ForeignKey('Post')
    author = models.CharField('Author', max_length=30)
    author_email = models.EmailField('Email', blank=True)
    author_url = models.URLField('Url', blank=True)
    author_ip = models.GenericIPAddressField('IP')
    datetime = models.DateTimeField('Date', auto_now_add=True)
    content = models.TextField('Content')
    parent = models.ForeignKey('self')

    def __str__(self):
        return self.content


class Category(models.Model):
    title = models.CharField('Title', max_length=30)
    alias = models.CharField('Alias', max_length=30, blank=True, unique=True, default=title)
    description = models.TextField('Description', blank=True)

    def __str__(self):
        return self.title
