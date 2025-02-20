from django.shortcuts import render, redirect
from accounts.forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.urls import reverse_lazy
from django.views.generic import FormView, View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from accounts.models import UserBookShopAccount
from accounts.forms import DepositMoneyForm, EditProfileForm
from transactions.models import Transaction
from core.views import send_email


class UserRegisterView(FormView):
    form_class = UserRegisterForm
    template_name = 'accounts/authentication_form.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        login(self.request, user)
        UserBookShopAccount.objects.create(user=user)

        messages.success(self.request, "Account Created Successfully")
        return super(UserRegisterView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('accounts:profile')

    def get_context_data(self, **kwargs):
        context = super(UserRegisterView, self).get_context_data(**kwargs)
        context['form_title'] = "Register"
        context['btn_title'] = "Register"
        return context

class UserLoginView(LoginView):
    template_name = 'accounts/authentication_form.html'

    def get_success_url(self):
        return reverse_lazy('accounts:profile')
    
    def get_context_data(self, **kwargs):
        context = super(UserLoginView, self).get_context_data(**kwargs)
        context['form_title'] = "Login"
        context['btn_title'] = "Login"
        return context

class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, "Logged out Successfully")
        return redirect('accounts:login')


class UserChangePasswordView(LoginRequiredMixin, FormView):
    form_class = PasswordChangeForm
    template_name = 'accounts/authentication_form.html'

    def get(self, request):
        form = PasswordChangeForm(user=request.user)
        return render(request, self.template_name, {'form': form, 'form_title': 'Change Password', 'btn_title': 'Change Password'})

    def post(self, request):
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()  
            update_session_auth_hash(request, user) 

            send_email(request.user, 0, "Goriber-BookShop: Security Alert!", "accounts/security_alert.html")

            messages.success(request, "Password changed successfully!")
            return redirect('accounts:profile') 
            
        return render(request, self.template_name, {'form': form})


class UserUpdateProfileView(LoginRequiredMixin, FormView):
    form_class = EditProfileForm
    template_name = 'accounts/authentication_form.html'
    success_url = reverse_lazy('accounts:profile')

    def get(self, request):
        form = EditProfileForm(instance=request.user)
        return render(request, self.template_name, {'form': form, 'form_title': 'Update Profile', 'btn_title': 'Update Profile'})

    def post(self, request):
        form = EditProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('accounts:profile')
        return render(request, self.template_name, {'form': form})


class DepositMoneyView(LoginRequiredMixin, FormView):
    form_class = DepositMoneyForm
    template_name = 'accounts/deposit_form.html'
    success_url = reverse_lazy('accounts:profile')

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')        
        user_account = UserBookShopAccount.objects.get(user=self.request.user)
        user_account.balance += amount

        user_account.save()
        Transaction.objects.create(
            user=self.request.user,
            amount=amount,
            trax_type='Deposit',
            action='Add Money',
            balance_after_transaction=user_account.balance
        )

        send_email(self.request.user, amount, "Deposit Successful!", "accounts/deposit_email.html")
        messages.success(self.request, f"Tk {amount} deposited successfully!")
        return super(DepositMoneyView, self).form_valid(form)
