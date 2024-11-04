from django.shortcuts import render, redirect, get_object_or_404
from .forms import EditProfile, CreateCampaign
from .models import Campaign
from .decorators import supervisor_required
from datetime import date
import logging

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
    return render(request, 'rewards.html', {})

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
    return render(request, 'campaigns.html', {
        'active_campaigns': active_campaigns,
        'inactive_campaigns': inactive_campaigns
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
def campaigns_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    today = date.today()  # Get today's date
    # Filter campaigns based on date
    active_campaigns = Campaign.objects.filter(start_date__lte=today, end_date__gte=today)
    inactive_campaigns = Campaign.objects.exclude(id__in=active_campaigns)

    print("Today's Date:", today)
    print("Active Campaigns Count:", active_campaigns.count())
    print("Inactive Campaigns Count:", inactive_campaigns.count())
    return render(request, 'campaigns.html', {
        'active_campaigns': active_campaigns,
        'inactive_campaigns': inactive_campaigns
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
def delete_campaign_view(request, id):
    campaign = get_object_or_404(Campaign, id=id)

    if request.method == "POST":
        # Log the delete action before deletion
        logger.debug(f"Campaign deleted by {request.user.username}: {campaign.name}")
        campaign.delete()
        return redirect('campaigns')

    return render(request, 'delete_campaign.html', {'campaign': campaign})