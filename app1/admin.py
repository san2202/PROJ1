import imp
from pkgutil import ModuleInfo
from django.contrib import admin
from app1.models import Student1, UserInfo,Student,P
# Register your models here.

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = [ 'id','name','email','contact','username','password','password1']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [ 'sid','sname','email','subject','contact']

@admin.register(Student1)
class Student1Admin(admin.ModelAdmin):
    list_display = [ 'sid','sname','fee','doj']

@admin.register(P)
class PAdmin(admin.ModelAdmin):
    list_display = [ 'sid','sname','courses']