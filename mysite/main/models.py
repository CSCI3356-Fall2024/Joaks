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
    minor = models.CharField(max_length=50, blank=True)
    double_minor = models.CharField(max_length=50, blank=True)
    referral = models.CharField(max_length=50, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    finished_profile = models.BooleanField(default=False)

class Campaign(models.Model):
    name = models.CharField(max_length=100)  # Name of the campaign
    description = models.TextField()  # Detailed description of the campaign
    start_date = models.DateField()  # Campaign start date
    end_date = models.DateField()  # Campaign end date
    locations = models.CharField(max_length=255)  # Places where the campaign is available
    points = models.IntegerField()  # Points associated with the campaign
    show_news = models.BooleanField(default=True)  # Boolean field to indicate if the campaign should be showed in the news feed
    integration_method = models.CharField(max_length=255)

    def __str__(self):
        return self.name