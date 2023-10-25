from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us', views.about_us, name='about_us'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('my_missions', views.my_missions, name='my_missions'),
    path('mission_available', views.mission_available, name='mission_available'),
    path('map', views.map, name='map'),
    path('settings', views.settings, name='settings'),
    path('partenaire', views.partenaire, name='partenaire'),
    path('login', views.login, name='login'),
    path('registration', views.registration, name='registration'),
    path('informations', views.informations, name='informations'),
]