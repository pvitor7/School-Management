from .views import ClassesIdView, ClassesListCreateView
from django.urls import path

urlpatterns = [
    path("", ClassesListCreateView.as_view()),
    path("<pk>/", ClassesIdView.as_view()),
]   