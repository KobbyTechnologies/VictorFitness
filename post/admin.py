from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['headline']
    }


# Register your models here.
admin.site.register(Post, PostAdmin)
