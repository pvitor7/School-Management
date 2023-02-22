from .views import CoursesIdView, CoursesListCreateView
from django.urls import path

urlpatterns = [
    path("campus/<str:campus_id>/courses/", CoursesListCreateView.as_view()),
    path("campus/<str:campus_id>/courses/<pk>/", CoursesIdView.as_view()),
]   