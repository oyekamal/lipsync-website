# Generated by Django 4.1.3 on 2022-12-07 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("applipsync", "0016_file_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="file",
            name="slug",
            field=models.SlugField(max_length=255),
        ),
    ]
