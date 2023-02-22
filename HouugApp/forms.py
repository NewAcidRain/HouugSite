from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserFrom(UserCreationForm):

    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-input1','placeholder': '  Никнейм'}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-input1','placeholder': '  ••••••••••••••••'}))
    password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput(attrs={'class': 'form-input1','placeholder': '  ••••••••••••••••'}))
    email = forms.CharField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-input1','placeholder': '  example@example.com'}))
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input1'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input1'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input1'}),
            'email': forms.EmailInput(attrs={'class': 'form-input1'})


        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин',widget=forms.TextInput(attrs={'class':'form-input2','placeholder': '  Никнейм'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-input2','placeholder': '  ••••••••••••••••'}))
