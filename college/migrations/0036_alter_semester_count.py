# Generated by Django 4.1.7 on 2023-09-20 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0035_year_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='count',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
