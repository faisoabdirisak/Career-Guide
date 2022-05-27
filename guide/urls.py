from django.urls import path;
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('careers', views.careers, name='careers'),
    path('career/<str:pk>/', views.career, name='career'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
  
]