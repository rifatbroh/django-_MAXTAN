from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    usable_password = None
    username = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required', 'placeholder' : 'Username', 'label' : ''}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required', 'placeholder' : 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required', 'placeholder' : 'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id' : 'required', 'placeholder' : 'E-mail'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'id' : 'required', 'placeholder' : 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'id' : 'required', 'placeholder' : 'Confirm Password'}))


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        fld = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        for f in fld:
            self.fields[f].help_text = None


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class UpdateProfileForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'id': 'required', 'placeholder': 'Username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'required', 'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'required', 'placeholder': 'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id': 'required', 'placeholder': 'E-mail'}))


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name in self.fields:
            self.fields[field_name].help_text = None

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
