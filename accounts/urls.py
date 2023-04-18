from django.urls import path
from . import views
#from .views import CustomLogoutView,MainView, RegisterView
from django.contrib.auth import views as auth_views


app_name = "accounts"

urlpatterns = [
    path('login/', views.user_login, name="login"),
    #path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('register/', views.register, name="register"),
    #path('', MainView.as_view(), name="main")
]
