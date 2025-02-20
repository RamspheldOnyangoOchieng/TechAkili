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
