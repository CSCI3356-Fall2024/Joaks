from django.contrib.auth.models import AbstractUser
from django.db import models
from .majors import MAJORS

# Create your models here.

class CustomUser(AbstractUser):
    CHOICES = (
        ('student', 'Student'), 
        ('supervisor', 'Supervisor'),
    )
    role = models.CharField(max_length=20, choices=CHOICES, default='student')
    class_year = models.CharField(max_length=50, blank=True)
    school = models.CharField(max_length=50, blank=True)
    major = models.CharField(max_length=50, choices=MAJORS, blank=True)
    double_major = models.CharField(max_length=50, choices=MAJORS, blank=True)
    minor = models.CharField(max_length=50, choices=MAJORS, blank=True)
    double_minor = models.CharField(max_length=50, choices=MAJORS, blank=True)
    referral = models.CharField(max_length=50, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    finished_profile = models.BooleanField(default=False)
    points = models.IntegerField(default=0)

class UpcomingEvents(models.Model):
    LOCATION_CHOICES = (
        ('BEAN', 'The Bean Counter'),
        ('CARNEY', 'Carney Dining Room'),
        ('CAFE129', 'Café 129'),
        ('CHOC', 'Chocolate Bar'),
        ('CORO', 'CoRo Café & Market'),
        ('EAGLES', "Eagle's Nest"),
        ('HILLSIDE', 'Hillside Café'),
        ('LEGAL', 'Legal Grounds'),
        ('ADDIES', "The Loft @ Addie's"),
        ('LOWER', 'Lower Live'),
        ('LYONS', 'Lyons Hall'),
        ('STUART', 'Stuart Dining Hall'),
        ('BAKERY', 'BC Bakery'),
        ('CONCESSIONS', 'Concessions'),
        ('MARKET', 'The Market'),
        ('TULLY', 'Tully Cafe'),
        ('BROOK', 'Brookline Campus Dining Hall'),
    )
    name = models.CharField(max_length=100)  # Name of the campaign
    description = models.TextField()  # Detailed description of the campaign
    start_date = models.DateField()  # Campaign start date
    end_date = models.DateField()  # Campaign end date
    locations = models.CharField(max_length=255)
    show_news = models.BooleanField(default=True)  # Boolean field to indicate if the campaign should be showed in the news feed
    integration_method = models.CharField(max_length=255)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='upcomingevents')
    image = models.ImageField(upload_to='events_images/', null=False, blank=False)  # Mandatory image field

    def __str__(self):
        return self.name


class Campaign(models.Model):
    LOCATION_CHOICES = (
        ('BEAN', 'The Bean Counter'),
        ('CARNEY', 'Carney Dining Room'),
        ('CAFE129', 'Café 129'),
        ('CHOC', 'Chocolate Bar'),
        ('CORO', 'CoRo Café & Market'),
        ('EAGLES', "Eagle's Nest"),
        ('HILLSIDE', 'Hillside Café'),
        ('LEGAL', 'Legal Grounds'),
        ('ADDIES', "The Loft @ Addie's"),
        ('LOWER', 'Lower Live'),
        ('LYONS', 'Lyons Hall'),
        ('STUART', 'Stuart Dining Hall'),
        ('BAKERY', 'BC Bakery'),
        ('CONCESSIONS', 'Concessions'),
        ('MARKET', 'The Market'),
        ('TULLY', 'Tully Cafe'),
        ('BROOK', 'Brookline Campus Dining Hall'),
    )
    name = models.CharField(max_length=100)  # Name of the campaign
    description = models.TextField()  # Detailed description of the campaign
    start_date = models.DateField()  # Campaign start date
    end_date = models.DateField()  # Campaign end date
    locations = models.CharField(max_length=255)  # Places where the campaign is available
    points = models.IntegerField()  # Points associated with the campaign
    show_news = models.BooleanField(default=True)  # Boolean field to indicate if the campaign should be showed in the news feed
    integration_method = models.CharField(max_length=255)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='campaigns')
    image = models.ImageField(upload_to='campaign_images/', null=False, blank=False)  # Mandatory image field



    def __str__(self):
        return self.name