# Generated by Django 3.2.6 on 2022-06-11 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(blank=True, max_length=100)),
                ('course_image', models.ImageField(blank=True, default='', upload_to='chat_imgs')),
                ('course_description', models.TextField(max_length=500)),
                ('course_created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courses_registered', models.TextField(default='', null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('test_of', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regional_women.course')),
            ],
        ),
        migrations.CreateModel(
            name='ques_ans_block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques', models.CharField(blank=True, max_length=100)),
                ('ans', models.CharField(max_length=100)),
                ('quest_ans_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regional_women.test')),
            ],
        ),
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(blank=True, default='', upload_to='chat_imgs')),
                ('lesson_of', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regional_women.course')),
            ],
        ),
    ]
