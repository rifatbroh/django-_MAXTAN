from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from accounts.models import DepositMoney

class UserRegisterForm(UserCreationForm):
    usable_password = None

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].help_text = None
            self.fields[field].widget.attrs.update({'required': True})


class EditProfileForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'id': 'required'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'required'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id': 'required'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name in self.fields:
            self.fields[field_name].help_text = None

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class DepositMoneyForm(forms.ModelForm):
    class Meta:
        model = DepositMoney
        fields = ['amount']

    def __init__(self, *args, **kwargs):
        super(DepositMoneyForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'required': True})
            self.fields[field].widget.attrs.update({'placeholder': 'Enter amount to deposit'})
            self.fields[field].help_text = None
    
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount < 100:
            raise forms.ValidationError("Amount must be at least 100")
        if amount > 100000:
            raise forms.ValidationError("Amount must be at most 100,000")
        return amount