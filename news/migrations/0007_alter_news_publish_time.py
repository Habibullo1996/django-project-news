# Generated by Django 4.2.1 on 2023-06-06 14:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_alter_news_image_alter_news_publish_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='publish_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 6, 14, 32, 8, 342321, tzinfo=datetime.timezone.utc)),
        ),
    ]
