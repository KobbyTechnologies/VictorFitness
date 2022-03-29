from django.contrib import admin
from .models import Program,Program_Detail,Topic,ProgramAttachments

# Register your models here.
admin.site.register(Program)
admin.site.register(Program_Detail)
admin.site.register(Topic)
admin.site.register(ProgramAttachments)

