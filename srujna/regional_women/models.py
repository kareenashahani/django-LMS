from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class user(models.Model):
    user = models.OneToOneField(User,related_name='user',on_delete=models.CASCADE,null=True)
    courses_registered = models.TextField(null=True,blank=True,default='')
    region = models.TextField(null=True,blank=True)
class Course(models.Model):
    course_name = models.CharField(max_length=100,blank=True)
    course_image = models.CharField(max_length=2000,blank=True,null=True)
    course_description = models.TextField(max_length=500,)
    course_created_date = models.DateTimeField(auto_now_add=True)
class Lessons(models.Model):
    name = models.CharField(max_length=100,blank=True)
    video_url = models.CharField(max_length=3000,blank=True,null=True)
    lesson_of = models.ForeignKey(Course,on_delete=models.CASCADE)
class Test(models.Model):
    name = models.CharField(max_length=100,blank=True)
    test_of = models.ForeignKey(Course,on_delete=models.CASCADE)
class ques_ans_block(models.Model):
    ques = models.CharField(max_length=100,blank=True)
    ans = models.CharField(max_length=100)
    quest_ans_to = models.ForeignKey(Test,on_delete=models.CASCADE)

class super_lady(models.Model):
    super_lady_user = models.OneToOneField(User,related_name='super_lady',on_delete=models.CASCADE,null=True)
    region = models.TextField(null=True,blank=True)

