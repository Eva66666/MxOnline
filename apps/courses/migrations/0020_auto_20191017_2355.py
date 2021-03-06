# Generated by Django 2.2 on 2019-10-17 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0019_auto_20191015_0208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=500, verbose_name='課程名'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='name',
            field=models.CharField(max_length=500, verbose_name='章節名'),
        ),
        migrations.AlterField(
            model_name='video',
            name='name',
            field=models.CharField(max_length=500, verbose_name='視頻名'),
        ),
    ]
