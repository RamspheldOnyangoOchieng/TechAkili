from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from django.contrib import messages
def home(request):
    return render(request, 'home.html')   # Template: home.html

def about(request):
    return render(request, 'about.html')  # Template: about.html

def services(request):
    return render(request, 'services.html')  # Template: services.html

def courses(request):
    return render(request, 'courses.html')  # Template: courses.html

def partners(request):
    return render(request, 'partners.html')  # Template: partners.html

def careers(request):
    return render(request, 'careers.html')  # Template: careers.html

def contact(request):
    return render(request, 'contact.html')  # Template: contact.html
def login(request):
    return render(request,'login.html')

def register(request):
    return render(request, 'register.html')

def submit_partnership(request):
    
    return render(request, 'submit_partnership.html')

def team(request):
    return render(request, 'ourteam.html')

def mission(request):
    return render(request, 'mission.html')
def training(request):
    return render(request, 'training.html')

def training_and_workshops(request):
    return render(request, 'training_and_workshops.html')

def consulting(request):
    return render(request, 'consulting.html')

def attarch(request):
    return render(request, 'attarch.html')

def intern(request):
    return render(request, 'intern.html')

def register_workshop(request):
    return render(request, 'register_workshop.html')

def workshop_detail(request):
    return render(request, 'workshop_detail.html')


def login_view(request):
    if request.method == 'POST':
        # Retrieve email and password from POST data.
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Note: If you’re using a custom user model with email as username,
        # ensure your authentication backend supports it.
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with the name of your homepage URL
        else:
            messages.error(request, "Invalid credentials, please try again.")
    return render(request, 'login.html')  # Your login template

def register_view(request):
    # Registration logic goes here.
    # For now, you can simply render a registration template.
    return render(request, 'register.html')

def forgot_password_view(request):
    # Forgot password logic goes here.
    return render(request, 'forgot_password.html')
