from re import search
from django.contrib import admin
from .models import MyUser

# Register your models here.
class  UserAdmin(admin.ModelAdmin):
    list_display = ('username','full_name','email','is_staff')
    search_fields = ('username','email','is_staff')
    list_per_page=25

admin.site.register(MyUser,UserAdmin)
