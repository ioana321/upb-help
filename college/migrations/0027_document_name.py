# Generated by Django 4.1.1 on 2022-10-05 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0026_alter_document_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='name',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
