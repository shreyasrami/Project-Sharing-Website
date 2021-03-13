from django.urls import path
from . import views

urlpatterns = [
    
    path('home/',views.home,name='home'),
    path('addpost/',views.addpost,name='addpost'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('team/',views.team,name='team'),
    path('profile/',views.profile,name='profile'),
    
]