# Generated by Django 4.1.7 on 2023-02-20 17:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0005_alter_post_publication_date_postlike'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 20, 22, 38, 17, 863180)),
        ),
        migrations.AlterField(
            model_name='postlike',
            name='liked_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 20, 22, 38, 17, 863180)),
        ),
    ]