# Generated by Django 3.2.6 on 2022-06-12 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regional_women', '0006_rename_image_lessons_video_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='video_url',
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
    ]
