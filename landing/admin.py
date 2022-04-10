from django.contrib import admin
from .models import Program,Program_Detail,Topic,ProgramAttachments
from  django.contrib.auth.models  import  Group 

# Register your models here.
class ProgramAdmin(admin.ModelAdmin):
    list_display=('Program_Type',)
    empty_value_display = '-none-'
class Program_DetailAdmin(admin.ModelAdmin):
    list_display = ('Program_Name','title','level','status','price','last_update')
    search_fields = ('Program_Name','title','status')
    list_per_page=25
    empty_value_display = '-none-'

    
class TopicAdmin(admin.ModelAdmin):
    list_display = ('video_title','program','last_update')
    search_fields = ('video_title','program')
    list_per_page=25
    empty_value_display = '-none-'
    
class ProgramAttachmentsAdmin(admin.ModelAdmin):
    list_display = ('file_name','program','last_update')
    search_fields = ('file_name','program')
    list_per_page=25
    empty_value_display = '-none-'
    
admin.site.register(Program,ProgramAdmin)
admin.site.register(Program_Detail,Program_DetailAdmin)
admin.site.register(Topic,TopicAdmin)
admin.site.register(ProgramAttachments,ProgramAttachmentsAdmin)
admin.site.unregister(Group)
