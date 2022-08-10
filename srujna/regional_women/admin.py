from django.contrib import admin
from .models import user,Course,Lessons,Test,ques_ans_block,super_lady
# Register your models here.

admin.site.register(user)
admin.site.register(Course)
admin.site.register(Lessons)
admin.site.register(Test)
admin.site.register(ques_ans_block)
admin.site.register(super_lady)
