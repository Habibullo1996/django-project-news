# Generated by Django 4.2.1 on 2023-06-06 02:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_contact_alter_news_publish_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to='media/news/images'),
        ),
        migrations.AlterField(
            model_name='news',
            name='publish_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 6, 2, 50, 22, 237947, tzinfo=datetime.timezone.utc)),
        ),
    ]
