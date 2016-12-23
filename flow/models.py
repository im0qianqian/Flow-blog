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
    post_title = models.CharField('Title', max_length=80, blank=True)
    post_content = models.TextField('Content', blank=True)
    post_alias = models.CharField('Alias', max_length=80, blank=True, unique=True, default=post_title)
    post_date = models.DateTimeField('Created time', auto_now_add=True, editable=True)
    post_modified = models.DateTimeField('Last Modified', auto_now=True, editable=True)

    def __str__(self):
        return self.post_title


class Post(models.Model):
    STATUS_CHOICES = (
        (True, 'Public'),
        (False, 'Hide')
    )
    post_author = models.ForeignKey(User)
    post_date = models.DateTimeField('Created time', auto_now_add=True, editable=True)
    post_modified = models.DateTimeField('Last Modified', auto_now=True, editable=True)
    post_title = models.CharField('Title', max_length=80, blank=True)
    post_content = models.TextField('Content', blank=True)
    post_excerpt = models.TextField('Excerpt', blank=True)
    post_status = models.BooleanField('Article status', default=False, choices=STATUS_CHOICES)
    post_password = models.CharField('Password', max_length=80, blank=True)
    post_alias = models.CharField('Alias', max_length=80, blank=True, unique=True, default=post_title)
    post_category = models.ForeignKey('Category')
    post_tag = models.ManyToManyField('Tag', blank=True)
    post_views = models.PositiveIntegerField('Pageviews', editable=False, default=0)
    post_image = models.URLField('Image', blank=True)

    def __str__(self):
        return self.post_title

    # Get the archives url. Maybe for duoshuo.
    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id': self.id})
        return "http://127.0.0.1:8000/%s" % path

    class Meta:
        ordering = ['-post_date']


class Link(models.Model):
    link_name = models.CharField('Name', max_length=30, blank=True)
    link_url = models.URLField('Url', unique=True)
    link_description = models.TextField('Description', blank=True)
    link_image = models.URLField('Image', blank=True)

    def __str__(self):
        return self.link_name


class Tag(models.Model):
    tag_name = models.CharField('Name', max_length=30)
    tag_alias = models.CharField('Alias', max_length=30, blank=True, unique=True, default=tag_name)

    def __str__(self):
        return self.tag_name


class Comment(models.Model):
    comment_post_id = models.ForeignKey('Post')
    comment_author = models.CharField('Author', max_length=30)
    comment_author_email = models.EmailField('Email', blank=True)
    comment_author_url = models.URLField('Url', blank=True)
    comment_author_ip = models.GenericIPAddressField('IP')
    comment_date = models.DateTimeField('Date', auto_now_add=True)
    comment_content = models.TextField('Content')
    comment_parent = models.ForeignKey('self')

    def __str__(self):
        return self.comment_content


class Category(models.Model):
    meta_name = models.CharField('Name', max_length=30)
    meta_alias = models.CharField('Alias', max_length=30, blank=True, unique=True, default=meta_name)
    meta_description = models.TextField('Description', blank=True)

    def __str__(self):
        return self.meta_name
