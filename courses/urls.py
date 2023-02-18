from .views import CoursesIdView, CoursesListCreateView
from django.urls import path

urlpatterns = [
    path("", CoursesListCreateView.as_view()),
    path("<pk>/", CoursesIdView.as_view()),
]   