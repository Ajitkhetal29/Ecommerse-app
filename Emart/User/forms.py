from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile , Review


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name =forms.CharField()
    last_name=forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'user','contact', 'locality', 'city','state','address','zipcode',]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'email', 'review']        