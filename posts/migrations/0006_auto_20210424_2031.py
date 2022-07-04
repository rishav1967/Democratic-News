# Generated by Django 3.2 on 2021-04-24 15:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0005_auto_20210424_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='bookmark',
            field=models.ManyToManyField(blank=True, related_name='bookmark', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='center',
            field=models.ManyToManyField(blank=True, related_name='center', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='fake_news',
            field=models.ManyToManyField(blank=True, related_name='fake_news', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='left',
            field=models.ManyToManyField(blank=True, related_name='left_wing', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='post_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='propaganda',
            field=models.ManyToManyField(blank=True, related_name='propagana', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='right',
            field=models.ManyToManyField(blank=True, related_name='right_wing', to=settings.AUTH_USER_MODEL),
        ),
    ]