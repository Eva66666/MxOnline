# Generated by Django 2.2 on 2019-10-19 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0022_auto_20191019_0028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='learn_times',
        ),
        migrations.RemoveField(
            model_name='video',
            name='learn_times',
        ),
    ]
