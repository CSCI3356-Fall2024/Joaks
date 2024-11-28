from django.contrib.auth.models import AbstractUser
from django.db import models
from .majors import MAJORS

# Create your models here.

class CustomUser(AbstractUser):
    CHOICES = (
        ('student', 'Student'), 
        ('supervisor', 'Supervisor'),
    )
    role = models.CharField(max_length=20, choices=CHOICES, default='student')  # Student or Supervisor
    class_year = models.CharField(max_length=50, blank=True)  # Graduation Year
    school = models.CharField(max_length=50, blank=True)  # Their School within BC
    major = models.CharField(max_length=50, choices=MAJORS, blank=True)  # First Major (req)
    double_major = models.CharField(max_length=50, choices=MAJORS, blank=True)  # Double Major
    minor = models.CharField(max_length=50, choices=MAJORS, blank=True)  # Minor
    double_minor = models.CharField(max_length=50, choices=MAJORS, blank=True)  # Double Minor
    referral = models.CharField(max_length=50, null=True, blank=True)  # The email of the user who referred them
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)  # Profile photo image
    finished_profile = models.BooleanField(default=False)  # Allows a new user to move on from edit profile page
    points = models.IntegerField(default=0)  # The amount of points the user has
    referral_points = models.IntegerField(default=0)  # The amount of times the user has been entered as a referral
    is_first_login = models.BooleanField(default=True)  # Track first login
    points_to_redeem = models.IntegerField(default=0) # Decrement this when points are redeemed, increment when points are earned, won't affect leaderboard
    completed_campaigns = models.ManyToManyField('Campaign', blank=True, related_name='completed_users')


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
    
class Milestone(models.Model):
    
    name = models.CharField(max_length=100)  # Name of the campaign
    description = models.TextField()  # Detailed description of the campaign
    show_news = models.BooleanField(default=True)  # Boolean field to indicate if the campaign should be showed in the news feed
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='milestones')
    image = models.ImageField(upload_to='milestones_images/', null=False, blank=False)  # Mandatory image field

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
    completed_by = models.ManyToManyField(CustomUser, related_name='completed_by_campaigns', blank=True) # Campaign completion tracker



    def __str__(self):
        return self.name

class Reward(models.Model):
    
    name = models.CharField(max_length=100)  # Name of the product
    point_value = models.IntegerField()  # Point value associated with the reward
    quantity = models.IntegerField()  # How many of these rewards available
    start_date = models.DateField()  # Reward start date
    end_date = models.DateField()  # Reward end date
    exchange_method = models.CharField(max_length=255)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='rewards')
    image = models.ImageField(upload_to='reward_images/', null=False, blank=False)  # Mandatory image field

    def __str__(self):
        return self.name

class RewardRedemption(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='redemptions')
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE)
    redemption_date = models.DateTimeField(auto_now_add=True)
    points_spent = models.IntegerField()
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], default='pending')

    def __str__(self):
        return f"{self.user.username} - {self.reward.name} ({self.redemption_date})"


class CampaignCompletion(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='completions')
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    completion_date = models.DateTimeField(auto_now_add=True)
    points_earned = models.IntegerField()
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], default='pending')

    def __str__(self):
        return f"{self.user.username} - {self.campaign.name} ({self.redemption_date})"

