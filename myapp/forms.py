from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . models import CustomUser

class RegisterForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=['username', 'first_name','last_name', 'email', 'mobile', 'password1', 'password2']
        widgets={
            'username':forms.TextInput(attrs={
                'class': 'form-control border-primary',
                'placeholder':'Enter user name'
            }),
            'first_name':forms.TextInput(attrs={
                'class': 'form-control border-primary',
                'placeholder':'Enter first name'
            }),
            'last_name':forms.TextInput(attrs={
                'class': 'form-control border-primary',
                'placeholder':'Enter last name'
            }),
            'email':forms.EmailInput(attrs={
                'class': 'form-control border-primary',
                'placeholder':'Enter first email'
            }),
            'mobile':forms.NumberInput(attrs={
                'class': 'form-control border-primary',
                'placeholder':'Enter contact number'
            }),
        }
    password1=forms.CharField(
                label=("Enter your password"),
                widget=forms.PasswordInput(attrs={
                    'class': 'form-control border-primary',
                    'placeholder':'Enter your password'}),
            )
    password2=forms.CharField(
                    label=("Enter your confirm password"),
                    widget=forms.PasswordInput(attrs={
                        'class': 'form-control border-primary',
                        'placeholder':'Enter your confirm password'}),
                )

class LoginForm(AuthenticationForm):
    username=forms.CharField(
        label=("Enter Username"),
        widget=forms.TextInput(attrs={
            'class': 'form-control border-primary',
            'placeholder':'Enter your username'}),
    )
    password=forms.CharField(
            label=("Enter your password"),
            widget=forms.PasswordInput(attrs={
                'class': 'form-control border-primary',
                'placeholder':'Enter your password'}),
        )
    