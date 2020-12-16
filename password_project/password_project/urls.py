
from django.urls import path
from password_generator import views

urlpatterns = [
    path('', views.home, name="home"),
    path('password', views.password),
    path('about', views.about, name='about')
]
