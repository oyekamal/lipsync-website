# Generated by Django 4.1.3 on 2022-11-30 05:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("applipsync", "0008_videoframe_video_frame_keys"),
    ]

    operations = [
        migrations.CreateModel(
            name="Video",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("video", models.FileField(upload_to="video/")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "video_frame",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="applipsync.videoframe",
                    ),
                ),
            ],
        ),
    ]
