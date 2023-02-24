from .views import ClassesIdView, ClassesListCreateView
from django.urls import path

urlpatterns = [
    path("campus/courses/<str:course_id>/classes/", ClassesListCreateView.as_view()),
    path("campus/courses/<str:course_id>/classes/<pk>/", ClassesIdView.as_view()),
]   