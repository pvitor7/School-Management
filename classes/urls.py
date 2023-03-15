from .views import ClassesIdView, ClassesListCreateView
from django.urls import path

urlpatterns = [
    path("campus/<str:campus_id>/courses/<str:course_id>/classes/", ClassesListCreateView.as_view(), name="classes-list-create-view"),
    path("campus/<str:campus_id>/courses/<str:course_id>/classes/<pk>/", ClassesIdView.as_view(), name="classes-retrive-view"),
]   