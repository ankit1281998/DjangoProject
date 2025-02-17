from django.urls import path, include
from . import views


urlpatterns = [
    path('hello/', views.print_hello),
    path('signup/', views.signup),
    path('login/', views.login),
    path('home/', views.home),
]