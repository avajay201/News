# Generated by Django 4.1.7 on 2023-03-02 17:27

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('post_image', models.ImageField(blank=True, upload_to='post')),
                ('summary', models.TextField(max_length=5000)),
                ('content', models.TextField(max_length=10000)),
                ('image_url', models.URLField(default='')),
                ('publication_date', models.DateTimeField(default=datetime.datetime(2023, 3, 2, 22, 57, 31, 874115))),
                ('author', models.CharField(max_length=250)),
                ('total_likes', models.IntegerField()),
                ('views', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Slider_Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_slider_image', models.ImageField(blank=True, upload_to='post')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.post')),
            ],
        ),
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked_date', models.DateTimeField(default=datetime.datetime(2023, 3, 2, 22, 57, 31, 889743))),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
