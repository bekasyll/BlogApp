import datetime
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView

from blog.models import Posts


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Username or E-mail:", required=True, max_length=30,
            widget=forms.TextInput(attrs={"class":"form-control", "aria-describedby":"emailHelp", "placeholder":"Enter your username or email"}))
    password = forms.CharField(label="Password:", required=True, max_length=30,
            widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":"Enter your password"}))

    class Meta:
        model = get_user_model()
        fields = ["username", "password"]


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Username:", max_length=30, required=True,
            widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Enter username"}))
    email = forms.EmailField(label="Email:", max_length=50, required=True,
            widget=forms.EmailInput(attrs={"class":"form-control", "placeholder": "Enter email"}))
    password1 = forms.CharField(label="Password:", max_length=30, required=True,
            widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder": "Enter password"}))
    password2 = forms.CharField(label="Password again:", max_length=30, required=True,
                                widget=forms.PasswordInput(
                                    attrs={"class": "form-control", "placeholder": "Enter password again"}))

    class Meta:
        fields = ['username', 'email', 'password1', 'password2']
        model = get_user_model()

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError("Passwords do not match!")
        return cd['password2']

    def clean_email(self):
        user_email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=user_email).exists():
            raise forms.ValidationError("Email already exists!")
        return user_email


class NewPostForm(forms.ModelForm):
    title = forms.CharField(label="Title:", required=True, max_length=30, widget=forms.TextInput(attrs={"class": "form-control", "aria-describedby": "emailHelp"}))
    content = forms.CharField(label="Content:", required=True, widget=forms.Textarea(attrs={"class": "form-control", "rows": 7}))

    class Meta:
        model = Posts
        fields = ['title', 'content']


class ProfileUserForm(forms.ModelForm):
    this_year = datetime.date.today().year
    username = forms.CharField(disabled=True, label="Username:", widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(disabled=True, label="E-mail:",
                             widget=forms.TextInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="First Name:", max_length=50, required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label="Last Name:", max_length=50, required=False, widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = get_user_model()
        fields = ["username", "email", "first_name", "last_name"]

class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="Old password:", max_length=30, required=True, widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter old password"}))
    new_password1 = forms.CharField(label="New password:", max_length=30, required=True, widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter new password"}))
    new_password2 = forms.CharField(label="New password again:", max_length=30, required=True, widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter new password again"}))