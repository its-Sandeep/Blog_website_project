# Generated by Django 3.1 on 2020-08-17 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0006_auto_20200817_0138'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click above link to view full post...', max_length=255),
        ),
    ]
