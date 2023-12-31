# Generated by Django 5.0 on 2023-12-29 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cycles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cycle',
            name='name',
        ),
        migrations.AddField(
            model_name='cycle',
            name='action_description',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='cycle',
            name='category',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cycle',
            name='check_description',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='cycle',
            name='do_description',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='cycle',
            name='plan_description',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='cycle',
            name='title',
            field=models.CharField(default='title', max_length=180),
        ),
    ]
