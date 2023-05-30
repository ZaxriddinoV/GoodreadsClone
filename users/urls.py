
from django.urls import path

from users.views import RegisterViews, LoginViews,ProfileView,LogoutView,ProfileUpdateView

app_name = "users"
urlpatterns = [
    path("register/", RegisterViews.as_view(), name="register"),
    path("login/",LoginViews.as_view(), name="login"),
    path('logout/',LogoutView.as_view(), name="logout"),
    path('profile/',ProfileView.as_view(), name='profile'),
    path('profile/edit/',ProfileUpdateView.as_view(), name='profile-edit'),
]