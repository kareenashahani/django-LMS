from django.shortcuts import render
from .models import Course,Lessons,user,super_lady
# Create your views here.
from django.views.generic import DeleteView

def user_courses(request):
    context = {
        "courses": Course.objects.all()
    }
    return render(request,'regional_women/user_courses.html',context)

def course(request,id):
    context = {
        "course": Course.objects.get(id = id),
        "lessons": Lessons.objects.filter(lesson_of=Course.objects.get(id = id))
    }
    return render(request,'regional_women/course.html',context)

def admin(request):
    context = {
        "superladies": super_lady.objects.all(),
        "users": user.objects.all()
    }
    return render(request,'regional_women/admindashboard.html',context)

#{% url 'course' course.id %}

class delete_user(DeleteView):
    model = user
    context_object_name='user'
    success_url= '/admindashboard'

class delete_superlady(DeleteView):
    model = super_lady
    context_object_name='s'
    success_url= '/admindashboard'
