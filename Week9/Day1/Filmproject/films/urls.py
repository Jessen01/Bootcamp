from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('homepage/',views.homepage,name='homepage'),
    path('addFilm/',views.addFilm,name='addFilm'),
    path('addDirector/',views.addDirector,name='addDirecto'),
    path('logout',views.Logout, name = 'logout')
#    path('logout/', auth_views.LogoutView.as_view(template_name='films/logout.html'), name='logout'),
]