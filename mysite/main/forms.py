from django import forms
from .models import CustomUser
from .majors import MAJORS
from .models import Campaign, UpcomingEvents, Milestone, Reward

class EditProfile(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['class_year', 'school', 'major', 'double_major', 'minor', 'double_minor', 'referral', 'profile_picture']
    CLASS_YEARS = [
        ('2025', '2025'), 
        ('2026', '2026'), 
        ('2027', '2027'), 
        ('2028', '2028'), 
        ('Postgrad', 'Postgrad')
    ]
    SCHOOLS = [
        ('MCAS', 'MCAS'), 
        ('CSOM', 'CSOM'), 
        ('LAW', 'LAW'), 
        ('WOODS', 'WOODS'), 
        ('BCSSW', 'BCSSW'), 
        ('CONNELL', 'Connell'), 
        ('LYNCH', 'Lynch'), 
        ('CSTM', 'CSTM'), 
        ('MESSINA', 'Messina')
    ]

    class_year = forms.ChoiceField(choices=CLASS_YEARS, required=True)
    school = forms.ChoiceField(choices=SCHOOLS, required=True)
    major = forms.ChoiceField(choices=MAJORS, required=True)
    double_major = forms.ChoiceField(choices=[('', '')] + list(MAJORS), required=False)
    minor = forms.ChoiceField(choices=[('', '')] + list(MAJORS), required=False)
    double_minor = forms.ChoiceField(choices=[('', '')] + list(MAJORS), required=False)
    referral = forms.CharField(max_length=50, required=False)
    profile_picture = forms.ImageField(required=False)

class CreateCampaign(forms.ModelForm):

    LOCATION_CHOICES = Campaign.LOCATION_CHOICES
    locations = forms.MultipleChoiceField(
        choices=LOCATION_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="OR Manually input locations",  # Custom label here
    )

    select_green2go = forms.BooleanField(
        required=False,
        label="Select All Green2Go Locations"
    )

    class Meta:
        model = Campaign
        fields = ['name', 'description', 'start_date', 'end_date', 'locations', 'points', 'show_news', 'integration_method', 'image', 'unlimited']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),  # HTML5 date picker
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

        def clean_locations(self):
            return ', '.join(self.cleaned_data['locations'])
        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['completed_by'].queryset = CustomUser.objects.none()
        
class CreateUpcomingEvents(forms.ModelForm):

    LOCATION_CHOICES = UpcomingEvents.LOCATION_CHOICES
    locations = forms.MultipleChoiceField(
        choices=LOCATION_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="OR Manually input locations",  # Custom label here
    )

    select_green2go = forms.BooleanField(
        required=False,
        label="Select All Green2Go Locations"
    )

    class Meta:
        model = UpcomingEvents
        fields = ['name', 'description', 'start_date', 'end_date', 'locations', 'show_news', 'integration_method', 'image']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),  # HTML5 date picker
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

        def clean_locations(self):
            return ', '.join(self.cleaned_data['locations'])
        
class CreateMilestone(forms.ModelForm):
    class Meta:
        model = Milestone
        fields = ['name', 'description', 'show_news', 'image']
        


class CreateReward(forms.ModelForm):

    LOCATION_CHOICES = Reward.LOCATION_CHOICES
    locations = forms.MultipleChoiceField(
        choices=LOCATION_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="OR Manually input locations",  # Custom label here
    )

    select_green2go = forms.BooleanField(
        required=False,
        label="Select All Green2Go Locations"
    )

  
    class Meta:
        model = Reward
        fields = ['name', 'point_value', 'quantity', 'locations', 'start_date', 'end_date', 'exchange_method', 'image']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

        def clean_locations(self):
            return ', '.join(self.cleaned_data['locations'])