import datetime

from django.conf import settings
from django.db import models
from django.utils import timezone

from ..profiles.models import Profile


class Post(models.Model):
    is_retweet = False
    content = models.CharField(max_length=255)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True, 
        blank=True
        )
    likes = models.IntegerField(default=0)
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Post updated at'
    )
    created = models.DateTimeField(
        auto_now=True,
        verbose_name='Post created at'
    )

    def readable_created(self):
        diff = timezone.now() - self.created

        if (diff.total_seconds() / 3600) <= 24:
            return "{} h".format(round(diff.total_seconds() / 3600))
        else:
            return self.created
    
    def set_is_retweet(self):
        self.is_retweet = True
    
    def has_comments(self):
        return self.comment_set.count() > 0
    
    def has_retweets(self):
        return self.retweet_set.count() > 0

    def has_likes(self):
        return self.likes > 0
    
    def get_comments(self):
        return self.comment_set.all().order_by('-created')

    def __str__(self):
        return self.content


class Comment(models.Model):
    content = models.CharField(max_length=255)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True, 
        blank=True)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )
    likes = models.IntegerField(default=0)
    created = models.DateTimeField(
        auto_now=True,
        verbose_name='Comment created at'
    )

    def readable_created(self):
        diff = timezone.now() - self.created

        if (diff.total_seconds() / 3600) <= 24:
            return "{} h".format(round(diff.total_seconds() / 3600))
        else:
            return self.created

    def __str__(self):
        return self.content


class Retweet(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True, 
        blank=True)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(
        auto_now=True,
        verbose_name='Retweeted at'
    )

    def readable_created(self):
        diff = timezone.now() - self.created

        if (diff.total_seconds() / 3600) <= 24:
            return "{} h".format(round(diff.total_seconds() / 3600))
        else:
            return self.created
    
    def is_retweet(self):
        return True

    def __str__(self):
        return self.post.content
