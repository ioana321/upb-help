# Generated by Django 4.1.1 on 2022-10-05 07:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0025_alter_document_content_type_alter_document_object_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='documents/', validators=[django.core.validators.FileExtensionValidator(['pdf'], 'Please upload a .pdf file!')]),
        ),
    ]
