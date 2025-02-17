from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('careers/', views.careers, name='careers'),
    path('contactus/', views.contactus, name='contactus'),
    path('courses/', views.courses, name='courses'),
]
