# Generated by Django 4.1.1 on 2022-09-26 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0014_alter_activity_options_remove_course_day_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='nr',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]