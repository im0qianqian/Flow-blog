from django.db import models
from .config import *
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Post(models.Model):
    STATUS_CHOICES = (
        (True, 'Public'),
        (False, 'Hide')
    )
    author = models.ForeignKey(User)
    created = models.DateTimeField('Created Time', auto_now_add=True, editable=True)
    modified = models.DateTimeField('Last Modified', auto_now=True, editable=True)
    title = models.CharField('Title', max_length=80)
    content = models.TextField('Content', blank=True)
    excerpt = models.TextField('Excerpt', blank=True)
    status = models.BooleanField('Article status', default=False, choices=STATUS_CHOICES)
    password = models.CharField('Password', max_length=80, blank=True)
    alias = models.CharField('Alias', max_length=80, blank=True, unique=True)
    category = models.ForeignKey('Category')
    tag = models.ManyToManyField('Tag', blank=True)
    views = models.PositiveIntegerField('Pageviews', editable=False, default=0)
    image = models.URLField('Image', blank=True)

    def __str__(self):
        return self.title

    # Get the archives url. Maybe for duoshuo.
    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id': self.id})
        return SITE_URL + path

    class Meta:
        ordering = ['-created']


class Page(models.Model):
    title = models.CharField('Title', max_length=80, blank=True)
    content = models.TextField('Content', blank=True)
    alias = models.CharField('Alias', max_length=80, blank=True, unique=True)
    created = models.DateTimeField('Created time', auto_now_add=True, editable=True)
    modified = models.DateTimeField('Last Modified', auto_now=True, editable=True)

    def __str__(self):
        return self.title

        # Get the archives url. Maybe for duoshuo.

    def get_absolute_url(self):
        path = reverse('post_meta', kwargs={'alias': self.alias})
        return SITE_URL + path

    class Meta:
        ordering = ['-created']


class Link(models.Model):
    title = models.CharField('Title', max_length=80)
    url = models.URLField('Url', unique=True)
    description = models.TextField('Description', blank=True)
    image = models.URLField('Image', blank=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField('Title', max_length=80)
    alias = models.CharField('Alias', max_length=80, blank=True, unique=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post_id = models.ForeignKey('Post')
    author = models.CharField('Author', max_length=80)
    author_email = models.EmailField('Email', blank=True)
    author_url = models.URLField('Url', blank=True)
    author_ip = models.GenericIPAddressField('IP')
    created = models.DateTimeField('Date', auto_now_add=True)
    content = models.TextField('Content')
    parent = models.ForeignKey('self')

    def __str__(self):
        return self.content


class Category(models.Model):
    title = models.CharField('Title', max_length=80)
    alias = models.CharField('Alias', max_length=80, blank=True, unique=True)
    description = models.TextField('Description', blank=True)
    parent = models.ForeignKey('self', default=1)

    def __str__(self):
        return self.title
