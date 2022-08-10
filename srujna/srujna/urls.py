"""srujna URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from super_lady import views as sviews
from regional_women import views as rviews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',sviews.login,name='login'),
    path('adduser',sviews.signup,name='adduser'),
    path('check_login',sviews.check_login,name='adduser'),
#    path('superlady_dashboard',sviews.registeredusers.as_view(template_name = 'super_lady/superlady.html'),name='superlady_dashboad'),
    path('superlady_dashboard',sviews.superlady_dashboad,name='superlady_dashboad'),
    path('assign_courses',sviews.assign_courses,name='assign_courses'),
    path('assign_roles',sviews.assign_roles,name='assign_roles'),
    path('user_courses',rviews.user_courses,name='user_courses'),
    path('course/<int:id>/',rviews.course,name='course'),
    path('admindashboard',rviews.admin,name="admindashboard"),
    path('delete_user/<int:pk>/',rviews.delete_user.as_view(template_name='regional_women/delete_user.html'),name="delete_user"),
    path('delete_superlady/<int:pk>/',rviews.delete_superlady.as_view(template_name='regional_women/delete_superlady.html'),name="delete_superlady")



]
