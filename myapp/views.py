# from django.shortcuts import render

# # Create your views here.
# def index(request):
#     return render(request,'logins/login.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser
import requests

def login_signup_view(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        # === LOGIN ===
        if form_type == 'login':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid email or password.')

        # === SIGNUP ===
        elif form_type == 'signup':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            if password != confirm_password:
                messages.error(request, 'Passwords do not match.')
            elif CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists.')
            else:
                user = CustomUser.objects.create_user(
                    username=email,
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name
                )
                messages.success(request, 'Account created successfully! You can now log in.')

    return render(request, 'logins/login.html')



@login_required(login_url='login')
def home(request):
    user = request.user
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        if form_type == 'manual':
            location_manual_input = request.POST.get('location')
            if not location_manual_input:
                messages.error(request, 'Please enter a valid location.')
            else:
                user.location = location_manual_input
                user.save()
                messages.success(request, f"Location '{location_manual_input}' saved successfully!")
                return redirect('main_page_weather')
        elif form_type == 'auto':
            lat = request.POST.get('latitude')
            lon = request.POST.get('longitude')
            location_auto_input = f"({lat},{lon})" if lat and lon else None
            if not location_auto_input:
                messages.error(request, 'Location access denied or unavailable.')
            else:
                print("Auto location input:", location_auto_input)  # Debugging line
                 # Save the location to the user's profile
                user.location = location_auto_input
                user.save()
                messages.success(request, f"Location '{location_auto_input}' saved successfully!")
                return redirect('main_page_weather')
        elif form_type =='use_prev':
            if user.location:
                messages.success(request, f"Using previously saved location '{user.location}'.")
                return redirect('main_page_weather')
            else:
                messages.error(request, 'No previously saved location found.')
                

    return render(request, 'logins/home.html')

@login_required(login_url='login')
def main_page_weather(request):
    user = request.user
    # user = request.user
    # check if location is available
    check_location = user.location
    if not check_location:
        messages.error(request, "No location found redirecting to /home")
        return redirect('home')
    else:
        location = user.location
        api_key = "f49ebbb8cbf67059d91c88a1f97ddfa9"
        url_for_open_weather_map = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
        response = requests.get(url_for_open_weather_map)
        data1 = response.json()
        print(data1)
        print(data1['name'])
        context ={
            'data':data1
        }
        return render(request, 'logins/main_weather_dashboard.html',context=context)
    
    