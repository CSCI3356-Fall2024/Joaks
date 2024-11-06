from django.contrib import admin
from .models import CustomUser, Campaign, UpcomingEvents, Milestone
# Register your models here.

@admin.register(CustomUser)
class CustomUser(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')
    list_filter = ('role',)

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'start_date', 'end_date', 'locations', 'points', 'show_news', 'integration_method')  


@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_by', 'show_news')  # Adjust fields as needed

@admin.register(UpcomingEvents)
class UpcomingEventsAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'description', 'start_date', 'end_date', 
        'locations', 'show_news', 'integration_method', 'created_by'
    )  # Specify fields to display in the admin list view

