from django.contrib import admin
from django.urls import path, include
from dashboard.views import index
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='index'),

    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='security/login.html'
        ),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(
            next_page='/login/'
        ),
        name='logout'
    ),
]