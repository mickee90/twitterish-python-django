from django.db import models


class Post(models.Model):
    content = models.CharField(max_length=255)
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    updated = models.DateTimeField('Post updated at')
    created = models.DateTimeField(
        auto_now=True,
        verbose_name='Post created at'
    )

    def __str__(self):
        return self.content


class Comment(models.Model):
    content = models.CharField(max_length=255)
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE)
    post_id = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )
    likes = models.IntegerField(default=0)
    created = models.DateTimeField(
        auto_now=True,
        verbose_name='Comment created at'
    )

    def __str__(self):
        return self.content


class Retweet(models.Model):
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(
        auto_now=True,
        verbose_name='Retweeted at'
    )

    def __str__(self):
        return self.post.content
