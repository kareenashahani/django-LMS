# Generated by Django 3.2.6 on 2022-06-12 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regional_women', '0004_auto_20220611_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_image',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
