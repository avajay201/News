# Generated by Django 4.1.7 on 2023-02-21 02:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0010_alter_post_publication_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 21, 8, 5, 56, 584788)),
        ),
        migrations.AlterField(
            model_name='postlike',
            name='liked_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 21, 8, 5, 56, 585790)),
        ),
    ]
