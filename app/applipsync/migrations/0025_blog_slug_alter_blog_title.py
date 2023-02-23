# Generated by Django 4.1.3 on 2023-02-04 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applipsync', '0024_category_tag_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default=2, max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]