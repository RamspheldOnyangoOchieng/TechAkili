from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def careers(request):
    return render(request, 'careers.html')

def contactus(request):
    return render(request, 'contactus.html')

def courses(request):
    return render(request, 'courses.html')
