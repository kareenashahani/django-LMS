# Generated by Django 3.2.6 on 2022-06-11 23:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('regional_women', '0002_alter_user_courses_registered'),
    ]

    operations = [
        migrations.CreateModel(
            name='super_lady',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('super_lady_user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='super_lady', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
