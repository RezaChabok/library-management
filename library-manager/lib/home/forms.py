from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'pls enter your username'}),
        label='username'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'pls enter your password'}),
        label='password'
    )
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        is_exists_username = User.objects.filter(username=username).exists()

        if not is_exists_username:
            raise forms.ValidationError('this is username not found or not register')
        else:
            return username