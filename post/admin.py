from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ['content']
    
    prepopulated_fields = {
        'slug': ['headline']
    }


# Register your models here.
admin.site.register(Post, PostAdmin)
