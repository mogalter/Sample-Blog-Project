from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)  # required = true by default

    class Meta:
        # gives us a nested namespace for configs and keeps them in one place
        # specify model you want to interact with
        model = User
        # fields we want to show on a form
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    # only want to update user/email
    class Meta:
        # gives us a nested namespace for configs and keeps them in one place
        # specify model you want to interact with
        model = User
        # fields we want to show on a form
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    # only want to update image
    class Meta:
        model = Profile
        fields = ['image']

