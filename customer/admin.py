from django.contrib import admin
#from django.conf import settings
from .models import UserInfo, SubscriptionPlan, SubscriptionFeatures, Gallery


# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ("names", "contacts", "gender",
                    "date_of_birth", "start_date")
    search_fields = ("names", "contacts")
    list_per_page = 25
    empty_value_display = "-none-"


admin.site.register(UserInfo, UserInfoAdmin)


class SubscriptionPlanAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'highlight_status', ]
    list_editable = ['highlight_status']
    sortable_by = ['price', ]


admin.site.register(SubscriptionPlan, SubscriptionPlanAdmin)


class SubscriptionFeaturesAdmin(admin.ModelAdmin):
    list_display = ['title', 'subscription_plans']

    def subscription_plans(self, obj):
        return ", " .join([sub.title for sub in obj.sub_plan.all()])


admin.site.register(SubscriptionFeatures, SubscriptionFeaturesAdmin)

class GalleryAdmin(admin.ModelAdmin):
    
    list_display = [
        'photo',
        'user',
        'date_added'
    ]

admin.site.register(Gallery, GalleryAdmin)
