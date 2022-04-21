from django.contrib import admin
#from django.conf import settings
from .models import UserInfo



# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
    list_display=("names","contacts", "gender","weight","height","date_of_birth","photos","goals","start_date")
    search_fields=("names","contacts")
    list_per_page=25
    empty_value_display="-none-"

admin.site.register(UserInfo,UserInfoAdmin)
    

