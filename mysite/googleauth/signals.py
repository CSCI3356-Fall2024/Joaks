from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.shortcuts import redirect
from django.urls import reverse
from .models import CustomUser

@receiver(user_logged_in)
def check_profile_completion(sender, request, user, **kwargs):
    # Check if the user's profile is incomplete
    if not user.finished_profile:
        # Redirect to profile completion page
        request.session['redirect_after_login'] = reverse('edit_profile')
    else:
        # Redirect to home page if profile is complete
        request.session['redirect_after_login'] = reverse('home')