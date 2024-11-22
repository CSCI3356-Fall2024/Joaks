from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    home_view, 
    actions_view,
    rewards_view,
    campaigns_view,
    profile_view,
    edit_profile_view,
    create_campaign_view,
    edit_campaign_view,
    delete_campaign_view,
    create_event_view,
    edit_event_view,
    delete_event_view,
    create_milestone_view,
    edit_milestone_view,
    delete_milestone_view,
    campaign_detail,
    event_detail,
    milestone_detail,
    all_campaigns_view,
    all_events_view,
    all_milestones_view,
    full_top_users_view,
    create_reward_view,
    edit_reward_view,
    delete_reward_view,
    redeem_reward_view,
    reward_history_view,
    complete_campaign_view,
    supervisor_rewards_view,
    supervisor_reward_history_view,  # Add this new import
)

urlpatterns = [
    path('', home_view, name='home'),
    path('actions/', actions_view, name='actions'),
    path('rewards/', rewards_view, name='rewards'),
    path('campaigns/', campaigns_view, name='campaigns'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', edit_profile_view, name='edit_profile'),
    path('campaigns/create/', create_campaign_view, name='create_campaign'),
    path('campaigns/<int:id>/edit/', edit_campaign_view, name='edit_campaign'),
    path('campaigns/<int:id>/delete/', delete_campaign_view, name='delete_campaign'),
    path('events/create/', create_event_view, name='create_event'),
    path('events/<int:id>/edit/', edit_event_view, name='edit_event'),
    path('events/<int:id>/delete/', delete_event_view, name='delete_event'),
    path('milestones/create/', create_milestone_view, name='create_milestone'),
    path('milestones/<int:id>/edit/', edit_milestone_view, name='edit_milestone'),
    path('milestones/<int:id>/delete/', delete_milestone_view, name='delete_milestone'),
    path('campaign/<int:campaign_id>/', campaign_detail, name='campaign_detail'),
    path('event/<int:event_id>/', event_detail, name='event_detail'),
    path('milestone/<int:milestone_id>/', milestone_detail, name='milestone_detail'),
    path('all-campaigns/', all_campaigns_view, name='all_campaigns'),
    path('all-events/', all_events_view, name='all_events'),
    path('all-milestones/', all_milestones_view, name='all_milestones'),
    path('leaderboard/', full_top_users_view, name='full_top_users'),
    path('rewards/create/', create_reward_view, name='create_reward'),
    path('rewards/<int:id>/edit/', edit_reward_view, name='edit_reward'),
    path('rewards/<int:id>/delete/', delete_reward_view, name='delete_reward'),
    path('rewards/<int:reward_id>/redeem/', redeem_reward_view, name='redeem_reward'),
    path('rewards/history/', reward_history_view, name='reward_history'),
    path('campaign/<int:campaign_id>/complete/', complete_campaign_view, name='complete_campaign'),
    path('supervisor/rewards/', supervisor_rewards_view, name='supervisor_rewards'),
    path('rewards/history/supervisor/', supervisor_reward_history_view, name='supervisor_reward_history'),  # Add this new URL pattern
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)