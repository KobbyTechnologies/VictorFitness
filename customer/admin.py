from django.contrib import admin
#from django.conf import settings
from .models import UserInfo, SubscriptionPlan, SubscriptionFeatures, Gallery, PersonalPlan,PersonalPlanFeature


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
    list_filter = ['sub_plan']

    def subscription_plans(self, obj):
        return ", " .join([sub.title for sub in obj.sub_plan.all()])

admin.site.register(SubscriptionFeatures, SubscriptionFeaturesAdmin)


class PersonalPlanAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'highlight_status', ]
    list_editable = ['highlight_status']
    sortable_by = ['price', ]

admin.site.register(PersonalPlan, PersonalPlanAdmin)

class PersonalPlanFeatureAdmin(admin.ModelAdmin):

    list_display = ['title', 'personal_plans']
    sortable_by = ['personal_plans']
    list_filter = ['sub_plan']

    def personal_plans(self, obj):
        return ", " .join([sub.title for sub in obj.sub_plan.all()])

admin.site.register(PersonalPlanFeature, PersonalPlanFeatureAdmin)

class GalleryAdmin(admin.ModelAdmin):
    
    list_display = [
        'photo',
        'user',
        'date_added'
    ]

admin.site.register(Gallery, GalleryAdmin)
