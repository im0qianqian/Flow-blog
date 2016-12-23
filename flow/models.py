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

class Post(models.Model):
    post_author = models.ForeignKey(User)
    post_date = models.DateTimeField(auto_now_add=True, editable=True)
    post_modified = models.DateTimeField(auto_now=True, editable=True)
    post_title = models.CharField(max_length=40, blank=True)
    post_content = models.TextField(blank=True)
    post_excerpt = models.TextField(blank=True)
    post_status = models.BooleanField(default=False)
    post_password = models.CharField(max_length=30, blank=True)
    post_alias = models.CharField(max_length=30, blank=True)
    post_category = models.ForeignKey('Category')
    post_tag = models.ManyToManyField('Tag', blank=True)
    post_image = models.URLField(blank=True)

    def __str__(self):
        return self.post_title

    # Get the archives url. Maybe for duoshuo.
    def get_absolute_url(self):
        path = self.post_alias + reverse('detail', kwargs={'id': self.id})
        return "http://127.0.0.1:8000/%s" % path


class Link(models.Model):
    link_url = models.URLField(unique=True)
    link_name = models.CharField(max_length=30, blank=True)
    link_description = models.TextField(blank=True)
    link_image = models.URLField(blank=True)
    link_category = models.ForeignKey('Category')

    def __str__(self):
        return self.link_name


class Tag(models.Model):
    tag_name = models.CharField(max_length=30)
    tag_alias = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.tag_name


class Comment(models.Model):
    comment_post_id = models.ForeignKey('Post')
    comment_author = models.CharField(max_length=30)
    comment_author_email = models.EmailField(blank=True)
    comment_author_url = models.URLField(blank=True)
    comment_author_ip = models.GenericIPAddressField()
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_content = models.TextField()
    comment_parent = models.ForeignKey('self')

    def __str__(self):
        return self.comment_content


class Category(models.Model):
    meta_name = models.CharField(max_length=30)
    meta_alias = models.CharField(max_length=30, blank=True)
    meta_description = models.TextField(blank=True)

    def __str__(self):
        return self.meta_name
