# Generated by Django 4.1.1 on 2022-10-03 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0018_document_activity_id_document_content_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='description',
        ),
    ]
