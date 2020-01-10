from django.contrib import admin

from .models import Post, Comment, Retweet

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Retweet)