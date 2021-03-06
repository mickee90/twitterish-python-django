# Generated by Django 3.0.1 on 2020-01-05 18:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Post updated at'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(auto_now=True, verbose_name='Comment created at'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now=True, verbose_name='Post created at'),
        ),
        migrations.AlterField(
            model_name='retweet',
            name='created',
            field=models.DateTimeField(auto_now=True, verbose_name='Retweeted at'),
        ),
    ]
