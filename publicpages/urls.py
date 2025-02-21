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
    path('register/', views.register, name='register'),        # Register Page
    path('submit_partnership/', views.submit_partnership, name ='submit_partnership'),
    path('team/',views.team, name='team'),
    path('mission/',views.mission, name='mission'),
    path('training/',views.training, name='training'),
    path('consulting/',views.consulting, name='consulting'),
    path('attarch/',views.attarch, name='attarch'),
    path('intern/',views.intern, name='intern'),
    path('training-and-workshops/', views.training_and_workshops, name='training_and_workshops'),
    path('register-workshop/', views.register_workshop, name='register_workshop'),
    path('workshop/<int:workshop_id>/', views.workshop_detail, name='workshop_detail'),
    path('forgot-password/', views.forgot_password_view, name='forgot_password')


]
