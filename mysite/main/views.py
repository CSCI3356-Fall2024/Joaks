from django.shortcuts import render, redirect
from .forms import EditProfile, CreateCampaign
from .models import Campaign
from datetime import date


# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    campaigns = Campaign.objects.all()
    context = {
        'campaigns' : campaigns
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


def create_campaign_view(request):
    if request.method == "POST":
        form = CreateCampaign(request.POST)
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

            campaign.save()
            return redirect('campaigns')
    else:
        form = CreateCampaign()

    return render(request, 'create_campaign.html', {'form': form})


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