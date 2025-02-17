from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                       # Home Page
    path('about/', views.about, name='about'),                # About Us Page
    path('services/', views.services, name='services'),       # Services Page
    path('courses/', views.courses, name='courses'),          # Courses Page
    path('partners/', views.partners, name='partners'),       # Partnerships Page
    path('careers/', views.careers, name='careers'),          # Careers Page
    path('contact/', views.contact, name='contact'),          # Contact Us Page
    path('login/', views.login, name='login'),                # Login Page
    path('register/', views.register, name='register')        # Register Page
]
