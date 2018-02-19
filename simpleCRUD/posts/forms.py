from django import forms
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget= forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name','last_name', 'bio','gender', 'email','password')