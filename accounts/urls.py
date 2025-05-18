from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path("login", views.user_login, name="login"),
    path("signup", views.user_signup, name="signup"),
    path("logout", views.user_logout, name="logout"),
    path("edit_profile", views.edit_profile, name="edit_profile"),
]
