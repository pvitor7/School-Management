from .views import SubjectsListCreateView, SubjectsIdView
from django.urls import path

urlpatterns = [
    path('campus/courses/<str:course_id>/subjects/', SubjectsListCreateView.as_view()),
    path('campus/courses/<str:course_id>/subjects/<pk>/', SubjectsIdView.as_view()),    
]   