# Generated by Django 3.0.1 on 2020-01-16 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='avatars/avatar_default.png', upload_to='avatars'),
        ),
    ]
