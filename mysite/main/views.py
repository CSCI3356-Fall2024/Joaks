from django.shortcuts import render, redirect, get_object_or_404
from .forms import EditProfile, CreateCampaign, CreateUpcomingEvents, CreateMilestone, CreateReward
from .models import Campaign, UpcomingEvents
from .models import CustomUser
from .models import UpcomingEvents
from .models import Milestone
from .models import Reward
from .decorators import supervisor_required
from datetime import date
import logging
from .models import RewardRedemption
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import models

logger = logging.getLogger('campaign_logger')


# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    campaigns = Campaign.objects.all()
    context = {
        'campaigns' : campaigns,
    }
    return render(request, 'home.html', context)


def actions_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, 'actions.html', {})


def rewards_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)

    today = date.today()

    active_rewards = Reward.objects.filter(start_date__lte=today, end_date__gte=today)
    inactive_rewards = Reward.objects.exclude(id__in=active_rewards)

    # Check if the user is a supervisor
    if request.user.is_authenticated and request.user.role == 'supervisor':
        template = 'supervisor_rewards.html'
    else:
        template = 'rewards.html'

    return render(request, template, {
        'active_rewards': active_rewards,
        'inactive_rewards': inactive_rewards,
    })


def rewards_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)

    today = date.today()

    # Get active rewards based on the current date
    active_rewards = Reward.objects.filter(start_date__lte=today, end_date__gte=today)
    inactive_rewards = Reward.objects.exclude(id__in=active_rewards)

    # Check if the user is authenticated and retrieve their points
    user_points = request.user.points if request.user.is_authenticated else 0

    # Separate active rewards into available and unavailable based on user points
    available_rewards = active_rewards.filter(point_value__lte=user_points)
    unavailable_rewards = active_rewards.exclude(id__in=available_rewards)

    # Choose the template based on user role
    template = 'supervisor_rewards.html' if request.user.is_authenticated and request.user.role == 'supervisor' else 'rewards.html'

    return render(request, template, {
        'available_rewards': available_rewards,
        'unavailable_rewards': unavailable_rewards,
        'active_rewards': active_rewards,
        'inactive_rewards': inactive_rewards,
    })

def all_campaigns_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    today = date.today()  # Get today's date
    # Filter campaigns based on date
    active_campaigns = Campaign.objects.filter(start_date__lte=today, end_date__gte=today)
    inactive_campaigns = Campaign.objects.exclude(id__in=active_campaigns)

    print("Today's Date:", today)
    print("Active Campaigns Count:", active_campaigns.count())
    print("Inactive Campaigns Count:", inactive_campaigns.count())
    return render(request, 'all_campaigns.html', {
        'active_campaigns': active_campaigns,
        'inactive_campaigns': inactive_campaigns
    })

def all_events_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    today = date.today()  # Get today's date
    # Filter campaigns based on date
    active_events = UpcomingEvents.objects.filter(start_date__lte=today, end_date__gte=today)
    inactive_events = UpcomingEvents.objects.exclude(id__in=active_events)

    print("Today's Date:", today)
    print("Active Events Count:", active_events.count())
    print("Inactive Events Count:", inactive_events.count())
    return render(request, 'all_events.html', {
        'active_events': active_events,
        'inactive_events': inactive_events
    })

def all_milestones_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    
    milestones = Milestone.objects.all()

    print("Active Events Count:", milestones.count())

    return render(request, 'all_milestones.html', {
        'milestones': milestones,
    })


def profile_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, 'profile.html', {'user' : request.user})




def edit_profile_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    
    user = request.user  # Get the logged-in user

    if request.method == "POST":
        form = EditProfile(request.POST, request.FILES, instance=user)  # Use the EditProfile form

        if form.is_valid():
            # Check if this is the user's first login
            if user.is_first_login:
                referral_email = form.cleaned_data.get('referral')
                
                if referral_email:
                    # Extract the username from the referral email
                    referral_username = referral_email.split('@')[0]
                    
                    # Find the referring user by username
                    referring_user = CustomUser.objects.filter(username=referral_username).first()
                    
                    if referring_user:
                        # Increment referral_points for the referring user
                        referring_user.referral_points += 1
                        referring_user.save()
                
                # Mark as not first login
                user.is_first_login = False

            form.save()  # Save the updated profile data

            # Check if the user's profile is incomplete, then mark it as finished
            if not user.finished_profile:
                user.finished_profile = True
                user.save()  # Save the updated user

            return redirect('profile')  # Redirect to the profile page after saving
    else:
        form = EditProfile(instance=user)  # Prepopulate form with current user data

    return render(request, 'edit_profile.html', {"form": form})


@supervisor_required
def create_campaign_view(request):
    if request.method == "POST":
        form = CreateCampaign(request.POST, request.FILES)
        if form.is_valid():
            campaign = form.save(commit=False)
            campaign.created_by = request.user

            # Check `select_green2go` using cleaned_data after form validation
            if form.cleaned_data.get('select_green2go'):
                # Set the Green2Go locations if the checkbox is checked
                green2go_locations = ['LOWER', 'CARNEY', 'STUART', 'ADDIES', 'EAGLES']
                campaign.locations = ', '.join(green2go_locations)
            else:
                # Save the user-selected locations
                campaign.locations = ', '.join(form.cleaned_data['locations'])

            # Log the create action
            logger.debug(f"Campaign created by {request.user.username}: {campaign.name}")
            campaign.save()
            return redirect('campaigns')
    else:
        form = CreateCampaign()

    return render(request, 'create_campaign.html', {'form': form})

@supervisor_required
def create_event_view(request):
    if request.method == "POST":
        form = CreateUpcomingEvents(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user

            # Check `select_green2go` using cleaned_data after form validation
            if form.cleaned_data.get('select_green2go'):
                # Set the Green2Go locations if the checkbox is checked
                green2go_locations = ['LOWER', 'CARNEY', 'STUART', 'ADDIES', 'EAGLES']
                event.locations = ', '.join(green2go_locations)
            else:
                # Save the user-selected locations
                event.locations = ', '.join(form.cleaned_data['locations'])

            # Log the create action
            logger.debug(f"Event created by {request.user.username}: {event.name}")
            event.save()
            return redirect('campaigns')
    else:
        form = CreateUpcomingEvents()

    return render(request, 'create_event.html', {'form': form})

@supervisor_required
def create_milestone_view(request):
    if request.method == "POST":
        form = CreateMilestone(request.POST, request.FILES)
        if form.is_valid():
            milestone = form.save(commit=False)
            milestone.created_by = request.user

            # Check `select_green2go` using cleaned_data after form validation
            # Log the create action
            logger.debug(f"Milestone created by {request.user.username}: {milestone.name}")
            milestone.save()
            return redirect('campaigns')
    else:
        form = CreateMilestone()

    return render(request, 'create_milestone.html', {'form': form})

@supervisor_required
def campaigns_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    today = date.today()  # Get today's date
    # Filter campaigns based on date
    active_campaigns = Campaign.objects.filter(start_date__lte=today, end_date__gte=today)
    inactive_campaigns = Campaign.objects.exclude(id__in=active_campaigns)

    active_events = UpcomingEvents.objects.filter(start_date__lte=today, end_date__gte=today)
    inactive_events = UpcomingEvents.objects.exclude(id__in=active_events)

    milestones = Milestone.objects.all()

    print("Today's Date:", today)
    print("Active Campaigns Count:", active_campaigns.count())
    print("Inactive Campaigns Count:", inactive_campaigns.count())
    print("Active Events Count:", active_events.count())
    print("Inactive Events Count:", inactive_events.count())
    print("Milestones Count: ", milestones.count())
    return render(request, 'campaigns.html', {
        'active_campaigns': active_campaigns,
        'inactive_campaigns': inactive_campaigns,
        'active_events': active_events,
        'inactive_events': inactive_events,
        'milestones' : milestones,
    })



@supervisor_required
def edit_campaign_view(request, id):
    campaign = get_object_or_404(Campaign, id=id)

    if request.method == "POST":
        form = CreateCampaign(request.POST, request.FILES, instance=campaign)
        if form.is_valid():
            campaign = form.save(commit=False)
            campaign.created_by = request.user

            # Check `select_green2go` using cleaned_data after form validation
            if form.cleaned_data.get('select_green2go'):
                # Set the Green2Go locations if the checkbox is checked
                green2go_locations = ['LOWER', 'CARNEY', 'STUART', 'ADDIES', 'EAGLES']
                campaign.locations = ', '.join(green2go_locations)
            else:
                # Save the user-selected locations
                campaign.locations = ', '.join(form.cleaned_data['locations'])

            # Log the edit action
            logger.debug(f"Campaign edited by {request.user.username}: {campaign.name}")

            campaign.save()
            return redirect('campaigns')
    else:
        form = CreateCampaign(instance=campaign)

    return render(request, 'edit_campaign.html', {'form': form, 'campaign': campaign})


@supervisor_required
def edit_event_view(request, id):
    event = get_object_or_404(UpcomingEvents, id=id)

    if request.method == "POST":
        form = CreateUpcomingEvents(request.POST, request.FILES, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user

            # Check `select_green2go` using cleaned_data after form validation
            if form.cleaned_data.get('select_green2go'):
                # Set the Green2Go locations if the checkbox is checked
                green2go_locations = ['LOWER', 'CARNEY', 'STUART', 'ADDIES', 'EAGLES']
                event.locations = ', '.join(green2go_locations)
            else:
                # Save the user-selected locations
                event.locations = ', '.join(form.cleaned_data['locations'])

            # Log the edit action
            logger.debug(f"Event edited by {request.user.username}: {event.name}")

            event.save()
            return redirect('campaigns')
    else:
        form = CreateUpcomingEvents(instance=event)

    return render(request, 'edit_event.html', {'form': form, 'event': event})

@supervisor_required
def edit_milestone_view(request, id):
    milestone = get_object_or_404(Milestone, id=id)

    if request.method == "POST":
        form = CreateMilestone(request.POST, request.FILES, instance=milestone)
        if form.is_valid():
            milestone = form.save(commit=False)
            milestone.created_by = request.user

            # Check `select_green2go` using cleaned_data after form validation

            # Log the edit action
            logger.debug(f"Milestone edited by {request.user.username}: {milestone.name}")

            milestone.save()
            return redirect('campaigns')
    else:
        form = CreateMilestone(instance=milestone)

    return render(request, 'edit_milestone.html', {'form': form, 'milestone': milestone})

@supervisor_required
def delete_campaign_view(request, id):
    campaign = get_object_or_404(Campaign, id=id)

    if request.method == "POST":
        # Log the delete action before deletion
        logger.debug(f"Campaign deleted by {request.user.username}: {campaign.name}")
        campaign.delete()
        return redirect('campaigns')

    return render(request, 'delete_campaign.html', {'campaign': campaign})

@supervisor_required
def delete_event_view(request, id):
    event = get_object_or_404(UpcomingEvents, id=id)

    if request.method == "POST":
        # Log the delete action before deletion
        logger.debug(f"Event deleted by {request.user.username}: {event.name}")
        event.delete()
        return redirect('campaigns')

    return render(request, 'delete_event.html', {'event': event})

@supervisor_required
def delete_milestone_view(request, id):
    milestone = get_object_or_404(Milestone, id=id)

    if request.method == "POST":
        # Log the delete action before deletion
        logger.debug(f"Event deleted by {request.user.username}: {milestone.name}")
        milestone.delete()
        return redirect('campaigns')

    return render(request, 'delete_milestone.html', {'milestone': milestone})

def campaign_detail(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    return render(request, 'campaign_detail.html', {'campaign': campaign})

def event_detail(request, event_id):
    event = get_object_or_404(UpcomingEvents, id=event_id)
    return render(request, 'event_detail.html', {'event': event})

def milestone_detail(request, milestone_id):
    milestone = get_object_or_404(Milestone, id=milestone_id)
    return render(request, 'milestone_detail.html', {'milestone': milestone})

def full_top_users_view(request):
    top_users = CustomUser.objects.filter(role='student').order_by('-points')
    top_referrers = CustomUser.objects.filter(role='student').order_by('-referral_points')
    return render(request, 'full_top_users.html', {'top_users': top_users, 'top_referrers' : top_referrers})


@supervisor_required
def create_reward_view(request):
    if request.method == "POST":
        form = CreateReward(request.POST, request.FILES)
        if form.is_valid():
            reward = form.save(commit=False)
            reward.created_by = request.user
            reward.save()

            # Log the creation action
            logger.debug(f"New Reward created by {request.user.username}: {reward.name}")

            return redirect('rewards')  # Redirect to the rewards list page
    else:
        form = CreateReward()  # Initialize the form for a GET request

    return render(request, 'create_reward.html', {'form': form})


@supervisor_required
def edit_reward_view(request, id):
    reward = get_object_or_404(Reward, id=id)
    if request.method == "POST":
        form = CreateReward(request.POST, request.FILES, instance=reward)
        if form.is_valid():
            form.save()
            logger.debug(f"Reward edited by {request.user.username}: {reward.name}")
            return redirect('supervisor_rewards')
    else:
        form = CreateReward(instance=reward)
    return render(request, 'edit_reward.html', {'form': form, 'reward': reward})

@supervisor_required
def delete_reward_view(request, id):
    reward = get_object_or_404(Reward, id=id)
    if request.method == "POST":
        logger.debug(f"Reward deleted by {request.user.username}: {reward.name}")
        reward.delete()
        return redirect('supervisor_rewards')
    return render(request, 'delete_reward.html', {'reward': reward})


@login_required
def redeem_reward_view(request, reward_id):
    if request.method == 'POST':
        reward = get_object_or_404(Reward, id=reward_id)
        user = request.user

        # Check if user has enough points
        if user.points < reward.point_value:
            messages.error(request, 'Not enough points to redeem this reward.')
            return redirect('rewards')

        # Check if reward is still available
        if reward.quantity <= 0:
            messages.error(request, 'This reward is out of stock.')
            return redirect('rewards')

        # Create redemption record
        redemption = RewardRedemption.objects.create(
            user=user,
            reward=reward,
            points_spent=reward.point_value
        )

        # Update user's points and reward quantity
        user.points_to_redeem -= reward.point_value
        user.save()
        reward.quantity -= 1
        reward.save()

        messages.success(request, f'Successfully redeemed {reward.name}!')
        return redirect('rewards')

    return redirect('rewards')

@login_required
def reward_history_view(request):
    redemptions = RewardRedemption.objects.filter(user=request.user).order_by('-redemption_date')
    return render(request, 'reward_history.html', {'redemptions': redemptions})

@login_required
def complete_campaign_view(request, campaign_id):
    print(f"Received campaign_id: {campaign_id}")

    if request.method == 'POST':
        campaign = get_object_or_404(Campaign, id=campaign_id)
        user = request.user

        # Makes sure campaign is only completed once
        if request.user in campaign.completed_by.all():
            messages.error(request, 'Campaign already completed.')
            return redirect('campaign_detail', campaign_id=campaign_id)
        
        # Maybe functionality to make sure it is still in redepmtion time?

        # Create campaign completion record

        # Update user's points and reward quantity
        user.points += campaign.points
        user.points_to_redeem += campaign.points
        user.save()
        campaign.completed_by.add(user)
        campaign.save()

        messages.success(request, f'Successfully completed {campaign.name}!')
        return redirect('campaign_detail', campaign_id=campaign_id)

    return redirect('campaign_detail', campaign_id=campaign_id)
