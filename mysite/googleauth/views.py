from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from main.models import Campaign
from main.models import CustomUser
from django.utils import timezone

# Login view
def login(request):
    return render(request, 'login.html')

def login(request):
    if request.user.is_authenticated:
        # Check if the user has finished their profile (or you can use a custom first_login field)
        if not request.user.finished_profile:
            # If profile is not complete, redirect to profile completion page
            return redirect('edit_profile')  # Replace with your profile completion URL
        else:
            # If profile is complete, redirect to home page
            return redirect('home')  # Replace with your home page URL
    else:
        # If user is not authenticated, render the login page
        return render(request, 'login.html')

# Home view (requires login)
#@login_required
#def home(request):
#    return render(request, 'home.html')

# Home view for both logged-in and logged-out users
def home(request):
    if request.user.is_authenticated:
        current_date = timezone.now().date()
        top_users = CustomUser.objects.filter(role='student').order_by('-points')[:5]
        top_referrers = CustomUser.objects.filter(role='student').order_by('-referral_points')[:5]
        
        # Filter for active campaigns with show_news=True
        active_campaigns = Campaign.objects.filter(
            start_date__lte=current_date,
            end_date__gte=current_date,
            show_news=True  # Only campaigns with show_news set to True
        )

        context = {
            'campaigns': active_campaigns,
            'top_users': top_users,
            'top_referrers': top_referrers,
        }
        return render(request, 'home_logged_in.html', context)  # Template for logged-in users
    else:
        return render(request, 'home_logged_out.html')  # Template for logged-out users

# Logout view
def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to home page or any other page