from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Login view
def login(request):
    return render(request, 'login.html')

# Home view (requires login)
#@login_required
#def home(request):
#    return render(request, 'home.html')

# Home view for both logged-in and logged-out users
def home(request):
    if request.user.is_authenticated:
        return render(request, 'home_logged_in.html')  # Template for logged-in users
    else:
        return render(request, 'home_logged_out.html')  # Template for logged-out users

# Logout view
def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to home page or any other page