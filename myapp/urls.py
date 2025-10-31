from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_signup_view, name='login'),
    path('home/', views.home, name='home'),
    path('main_page_weather/', views.main_page_weather, name='main_page_weather'),
]
