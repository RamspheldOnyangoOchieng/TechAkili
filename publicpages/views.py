from django.shortcuts import render

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
