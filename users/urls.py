from .views import UserCreateView, LoginView, UserIdView, UserListView
from django.urls import path

urlpatterns = [
    path("login/", LoginView.as_view(), name="login-view"),
    path("users/register/", UserCreateView.as_view(), name="user-create-view"),
    path("users/<pk>/", UserIdView.as_view(), name="user-retrive-view"),
    path("users/", UserListView.as_view(), name="list-users-view"),
]   