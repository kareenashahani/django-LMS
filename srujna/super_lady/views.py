from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from regional_women.models import user,Course,super_lady
# Create your views here.
from django.contrib import messages
def login(request):
    return render(request,'super_lady/index.html')
def check_login(request):
    user_id = request.POST.get('userid', False)
    password = request.POST.get('password', False)
    if User.objects.filter(username=user_id).exists():
        U = User.objects.get(username=user_id)
        if U.check_password(password):
            if user_id[0]=='u':
                return redirect('/user_courses')
            elif user_id[0]=='s':
                return redirect('/superlady_dashboard')
            else:
                return redirect('/admindashboard')
        else:
            return HttpResponse('Invalid userid or password!')
    else:
            return HttpResponse('Invalid userid or password!')

def signup(request):
    return render(request,'super_lady/signup.html')

def superlady_dashboad(request):
    context={
        'courses': Course.objects.all(),
        'users':user.objects.all()
    }

    return render(request,'super_lady/superlady.html',context=context)

def assign_courses(request):
    user_id = request.POST['woman_id']
    courses_assigned = request.POST['courses_assigned']
    
    U = User.objects.filter(username=user_id).first()
    uu = user.objects.get(user = U)
    u = user.objects.filter( user=U).update(courses_registered = uu.courses_registered + courses_assigned + ',')
    return redirect('/superlady_dashboard')

def assign_roles(request):

    name = request.POST['Name']
    user_id = request.POST['userid']
    region = request.POST['region']
    role = request.POST['role']
    password = request.POST['password']

    if user_id[0] != 's':
        if role == "2":
            User.objects.create(username=name,password=password)
            U = User.objects.get(username=name)
            s = super_lady.objects.create(super_lady_user=U,region=region)
        return redirect('/admindashboard')
    elif user_id[0] == 's':
        if role == "2":
            return HttpResponse("Access Denied")
        elif role=="3":
            User.objects.create(username=name,password=password)
            U = User.objects.get(username=name)
            u = user.objects.create(user=U,region=region)
        return redirect('/superlady_dashboard')





