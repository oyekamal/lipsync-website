# Generated by Django 4.1.3 on 2022-12-12 10:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applipsync', '0017_alter_file_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='audio',
            field=models.FileField(upload_to='audio/', validators=[django.core.validators.FileExtensionValidator(['wav'])]),
        ),
        migrations.AlterField(
            model_name='file',
            name='script',
            field=models.FileField(upload_to='script/', validators=[django.core.validators.FileExtensionValidator(['txt'])]),
        ),
    ]
