from django.shortcuts import render, redirect
from .forms import EditProfile

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
    user = request.user
    if request.method == "POST":
        form = EditProfile(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfile(instance=user)
    return render(request, 'edit_profile.html', {"form":form})