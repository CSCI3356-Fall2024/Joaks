from django import forms
from .models import CustomUser
from .majors import MAJORS

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
    