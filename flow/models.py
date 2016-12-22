from django.db import models
from flow.config import *


class User(models.Model):
    user_nickname = models.CharField(max_length=30)
    user_login = models.CharField(max_length=30)
    user_pass = models.CharField(max_length=40)
    user_email = models.EmailField(unique=True)
    user_url = models.URLField(max_length=50)
    user_registered = models.DateTimeField(auto_now_add=True)
    key_grade = models.IntegerField(default=GRADE_KEY['contributors'])


class Post(models.Model):
    post_author = models.ForeignKey('User')
    post_date = models.DateTimeField(auto_now_add=True, editable=True)
    post_modified = models.DateTimeField(auto_now=True, editable=True)
    post_title = models.CharField(max_length=40)
    post_content = models.TextField()
    post_excerpt = models.TextField()
    post_status = models.BooleanField(default=False)
    post_password = models.CharField(max_length=30)
    post_name = models.CharField(max_length=30)
    # Now have some thing ...


class Link(models.Model):
    link_url = models.URLField()
    link_name = models.CharField(max_length=30)
