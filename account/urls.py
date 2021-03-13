from django.urls import path
from . import views

urlpatterns = [
    path('',views.about,name='about'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('signup/',views.register,name='signup'),
    
]