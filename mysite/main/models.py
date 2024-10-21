from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    CHOICES = (
        ('student', 'Student'), 
        ('supervisor', 'Supervisor'),
    )
    role = models.CharField(max_length=20, choices=CHOICES, default='student')
    class_year = models.CharField(max_length=50, blank=True)
    school = models.CharField(max_length=50, blank=True)
    major = models.CharField(max_length=50, blank=True)
    double_major = models.CharField(max_length=50, blank=True)
    referral = models.CharField(max_length=50, blank=True)

