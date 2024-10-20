from django.contrib import admin
from .models import CustomUser
# Register your models here.

@admin.register(CustomUser)
class CustomUser(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')
    list_filter = ('role',)
