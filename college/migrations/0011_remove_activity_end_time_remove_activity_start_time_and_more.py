# Generated by Django 4.1.1 on 2022-09-23 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0010_day_activity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='start_time',
        ),
        migrations.AddField(
            model_name='activity',
            name='end_hour',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activity',
            name='start_hour',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
