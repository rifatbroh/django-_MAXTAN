from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, update_session_auth_hash, authenticate
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, AuthenticationForm
from django.contrib.auth.models import User
from user_app.forms import RegistrationForm, UpdateProfileForm

# Create your views here.
def home_view(request):
    return render(request, 'user_app/home.html')

def profile_view(request, username):
    if request.user.is_authenticated:
        if request.user.username != username:
            return redirect('home')
        
        user = User.objects.get(username=username)
        return render(request, 'user_app/profile.html')

    else:
        return redirect('login')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('profile', username=request.user.username)

    form = AuthenticationForm(request)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f"Successfully Logged in. Welcome {username}!")
                return redirect('profile', username=username)

    return render(request, 'user_app/all_form.html', {'form' : form, 'title' : 'Login', 'btn_txt' : 'Login'})
    
def register_view(request):
    if request.user.is_authenticated:
        return redirect('profile', username=request.user.username)
    
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Registration Successfull. Welcome, {user.username}!")
            return redirect('profile', username=request.user.username)
    return render(request, 'user_app/all_form.html', {'form' : form, 'title' : 'Register', 'btn_txt' : 'Register'})


def edit_profile_view(request, username):
    if request.user.is_authenticated:
        if request.user.username != username:
            return redirect('profile', username=request.user.username)
        
        form = UpdateProfileForm(instance=request.user)
        if request.method == 'POST':
            form = UpdateProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, "Profile Information Updated Successfully!")
                return redirect('profile', username=form.instance.username)
        
        return render(request, 'user_app/all_form.html', {'form' : form, 'title' : 'Edit Your Profile', 'btn_txt' : 'Save Changes'})

    else:
        return redirect('login')

def change_password_view(request, username):
    if request.user.is_authenticated:
        if request.user.username != username:
            return redirect('profile', username=request.user.username)
        
        form = PasswordChangeForm(request.user)
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, "Password Updated Successfully!")
                return redirect('profile', username=request.user.username)
        
        return render(request, 'user_app/all_form.html', {'form' : form, 'title' : 'Change Your Password', 'btn_txt' : 'Save Changes'})
    
    else:
        return redirect('login')


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logout Successfull!")
        return redirect('login')
    else:
        return redirect('login')