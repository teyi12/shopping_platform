from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, LoginForm, UserProfileForm
from .models import UserProfile



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            # Create UserProfile
            UserProfile.objects.create(
                user=user,
                address=form.cleaned_data['address'],
                phone_number=form.cleaned_data['phone_number']
            )
            login(request, user)
            return redirect('home')  # Redirect to a success page
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        address = request.POST.get('address', '')
        phone = request.POST.get('phone', '')
        image = request.FILES.get('image')

        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/register.html', {'error': 'Benutzername existiert bereits.'})

        user = User.objects.create_user(username=username, email=email, password=password)
        profile = UserProfile.objects.create(
            user=user,
            address=address,
            phone=phone,
            image=image
        )

        login(request, user)
        return redirect('home')  # oder dein gewünschter Start-View

    return render(request, 'accounts/register.html')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('accounts:profile')
            else:
                return render(request, 'accounts/login.html', {
                    'form': form,
                    'error': 'Invalid username or password'
                })
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')  # Redirect to the profile page
    else:
        form = UserProfileForm(instance=user_profile, user=request.user)
    return render(request, 'accounts/profile.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('accounts:login')






# Profilansicht
@login_required
def profile_view(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'accounts/profile.html', {'user_profile': user_profile})

