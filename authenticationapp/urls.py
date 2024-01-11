from django.urls import path
from .import views

urlpatterns = [
    path('',views.LoginView),
    path('login',views.LoginView,name='LoginView'),
    path('signup',views.SignUp,name='SignUp'),
    path('logout',views.LogoutView,name='LogoutView'),
]

# here LoginView is used twice to avoid reversible error