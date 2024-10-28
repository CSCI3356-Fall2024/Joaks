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
            form.save()  # Save the form data to create a new campaign
            return redirect('campaigns')  # Redirect to a success page
    else:
        form = CreateCampaign()  # Render an empty form

    return render(request, 'create_campaign.html', {'form': form})
