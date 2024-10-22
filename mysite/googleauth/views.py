from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Login view
def login(request):
    return render(request, 'login.html')

# Home view (requires login)
@login_required
def home(request):
    return render(request, 'home.html')

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page or any other page