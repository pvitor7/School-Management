from .views import UserCreateView, LoginView, UserIdView, UserListView
from django.urls import path

urlpatterns = [
    path("login/", LoginView.as_view()),
    path("users/register/", UserCreateView.as_view()),
    path("users/<pk>/", UserIdView.as_view()),
    path("users/", UserListView.as_view()),
]   