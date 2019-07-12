from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control badge-pill','placeholder':'Username'})
        self.fields['email'].widget.attrs.update({'class':'form-control badge-pill','placeholder':'Email'})
        self.fields['password1'].widget.attrs.update({'class':'form-control badge-pill','placeholder':'Password'})
        self.fields['password2'].widget.attrs.update({'class':'form-control badge-pill','placeholder':'Confirm Password'})
    

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username' , 'email' ]


class ProfileUpdateForm(forms.ModelForm):
    display_name = forms.CharField()

    class Meta:
        model = Profile
        fields = ['display_name']

class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image']
