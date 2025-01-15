from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import SignUpForm
from .models import Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout

# Create your views here.


def profile(request):
    return HttpResponse("This is the user profile")

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            

            # Create user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            # Create profile
            profile = Profile.objects.create(username=username, email=email, phone_number=phone_number)
            profile.save()

            return redirect('login')
    else:
        form = SignUpForm()
        
        
    if request.method == 'POST':
        loginform = AuthenticationForm(request, request.POST)
        if loginform.is_valid():
            user = loginform.get_user()
            auth_login(request, user)
            return redirect('profile')
        
    else:
        loginform = AuthenticationForm()
        
    # context = {
    #     'form': form,
    #     'loginform': loginform,
    # }
    return render(request, 'users/signup.html', context={'form': form, 'loginform': loginform})

# def login(request):
#     elif request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             auth_login(request, user)
#             return redirect('profile')  # Redirect to home page after login
    
#         form = AuthenticationForm()
     
#     return render(request, 'users/signup.html', {'form': form})