# Generated by Django 4.1.7 on 2023-09-20 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0037_alter_semester_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='year',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='semesters', to='college.year'),
        ),
    ]
