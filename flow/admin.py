from django import forms
from django.contrib import admin
from flow.models import *

# Register your models here.


admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(PostMeta)
admin.site.register(Link)
admin.site.register(Comment)
