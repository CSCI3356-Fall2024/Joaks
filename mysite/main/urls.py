from django.contrib import admin
from django.urls import path
from .views import home_view, actions_view, rewards_view, profile_view, campaigns_view, edit_profile_view

urlpatterns = [
    path('actions/', actions_view, name='actions'),
    path('', home_view, name='home'),
    path('rewards/', rewards_view, name='rewards'),
    path('profile/', profile_view, name='profile'),
    path('campaigns/', campaigns_view, name='campaigns'),
    path('edit-profile/', edit_profile_view, name="edit_profile"),
]
