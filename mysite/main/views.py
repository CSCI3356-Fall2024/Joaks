from django.shortcuts import render, redirect
from .forms import EditProfile, CreateCampaign

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, 'home.html', {})


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


def campaigns_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, 'campaigns.html', {})



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
            campaign = form.save(commit=False)  # Create instance but don’t save to DB yet
            campaign.created_by = request.user # Set the current user as the creator
            form.save()
            return redirect('campaigns')
    else:
        # Initialize the form with Green2Go locations if requested
        initial_data = {}
        if request.GET.get('select_green2go') == '1':  # Set Green2Go locations
            initial_data['locations'] = ['NY', 'SF', 'HOU']  # Set based on Green2Go locations
        form = CreateCampaign(initial=initial_data)

    return render(request, 'create_campaign.html', {'form': form})