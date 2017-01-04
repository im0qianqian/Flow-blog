from django.contrib import admin
from flow.models import *
from django.contrib.auth.models import User


class PostAdmin(admin.ModelAdmin):
    # Post admin list
    exclude = ('author',)
    list_display = ('title', 'author', 'category', 'created', 'status', 'views',)
    search_fields = ('title', 'excerpt',)
    list_filter = ('category',)
    filter_horizontal = ('tag',)

    """
    Overrides save_model
    if alias is null ,default = title.Author is current user.
    """

    def save_model(self, request, obj, form, change):
        obj.author = User(request.user.id)
        if obj.alias == '':
            obj.alias = obj.title
        obj.save()


admin.site.register(Post, PostAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'alias', 'parent',)

    def save_model(self, request, obj, form, change):
        if obj.alias == '':
            obj.alias = obj.title
        obj.save()


admin.site.register(Category, CategoryAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'alias',)

    def save_model(self, request, obj, form, change):
        if obj.alias == '':
            obj.alias = obj.title
        obj.save()


admin.site.register(Tag, TagAdmin)


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'alias', 'created', 'modified',)

    def save_model(self, request, obj, form, change):
        if obj.alias == '':
            obj.alias = obj.title
        obj.save()


admin.site.register(Page, PageAdmin)


class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url',)


admin.site.register(Link, LinkAdmin)


class CommentAdmin(admin.ModelAdmin):
    # list_display = ()
    pass


admin.site.register(Comment, CommentAdmin)
