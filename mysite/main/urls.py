from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import home_view, actions_view, rewards_view, profile_view, campaigns_view, edit_profile_view, create_campaign_view, edit_campaign_view, delete_campaign_view, all_campaigns_view, campaign_detail, create_event_view, event_detail, all_events_view, edit_event_view, delete_event_view, create_milestone_view, edit_milestone_view, delete_milestone_view, milestone_detail, all_milestones_view, create_reward_view, edit_reward_view, delete_reward_view, redeem_reward_view, reward_history_view, full_top_users_view

urlpatterns = [
    path('actions/', actions_view, name='actions'),
    path('', home_view, name='home'),
    path('rewards/', rewards_view, name='rewards'),
    path('profile/', profile_view, name='profile'),
    path('campaigns/', campaigns_view, name='campaigns'),
    path('edit-profile/', edit_profile_view, name="edit_profile"),
    path('create-campaign/', create_campaign_view, name='create_campaign'),
    path('campaigns/edit/<int:id>/', edit_campaign_view, name='edit_campaign'),
    path('campaigns/delete/<int:id>/', delete_campaign_view, name='delete_campaign'),
    path('all-campaigns/', all_campaigns_view, name='all_campaigns'),
    path('all-events/', all_events_view, name='all_events'),
    path('campaign/<int:campaign_id>/', campaign_detail, name='campaign_detail'),
    path('event/<int:event_id>/', event_detail, name='event_detail'),
    path('create-event/', create_event_view, name='create_event'),
    path('events/edit/<int:id>/', edit_event_view, name='edit_event'),
    path('events/delete/<int:id>/', delete_event_view, name='delete_event'),
    path('create-milestone/', create_milestone_view, name='create_milestone'),
    path('milestone/edit/<int:id>/', edit_milestone_view, name='edit_milestone'),
    path('milestone/delete/<int:id>/', delete_milestone_view, name='delete_milestone'),
    path('milestone/<int:milestone_id>/', milestone_detail, name='milestone_detail'),
    path('all-milestones/', all_milestones_view, name='all_milestones'),
    path('create-reward/', create_reward_view, name='create_reward'),
    path('rewards/edit/<int:id>/', edit_reward_view, name='edit_reward'),
    path('rewards/delete/<int:id>/', delete_reward_view, name='delete_reward'),
    path('rewards/redeem/<int:reward_id>/', redeem_reward_view, name='redeem_reward'),
    path('rewards/history/', reward_history_view, name='reward_history'),
    path('leaderboard/top_users/', full_top_users_view, name='full_top_users'),
]


if settings.DEBUG:  # Only serve media files in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)