from django.contrib import admin
from .models import CustomUser, Campaign
# Register your models here.

@admin.register(CustomUser)
class CustomUser(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')
    list_filter = ('role',)

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'start_date', 'end_date', 'locations', 'points', 'show_news', 'integration_method')  

