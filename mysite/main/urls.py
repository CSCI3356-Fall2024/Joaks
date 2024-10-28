from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import home_view, actions_view, rewards_view, profile_view, campaigns_view, edit_profile_view, create_campaign_view

urlpatterns = [
    path('actions/', actions_view, name='actions'),
    path('', home_view, name='home'),
    path('rewards/', rewards_view, name='rewards'),
    path('profile/', profile_view, name='profile'),
    path('campaigns/', campaigns_view, name='campaigns'),
    path('edit-profile/', edit_profile_view, name="edit_profile"),
    path('create-campaign/', create_campaign_view, name='create_campaign'),
]

if settings.DEBUG:  # Only serve media files in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)