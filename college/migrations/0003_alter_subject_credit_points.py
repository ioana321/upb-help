# Generated by Django 4.1.1 on 2022-09-19 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0002_subject_credit_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='credit_points',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
