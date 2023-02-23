from .views import SubjectsListCreateView, SubjectsIdView
from django.urls import path

urlpatterns = [
    path("", SubjectsListCreateView.as_view()),
    path("<pk>/", SubjectsIdView.as_view()),
    
]   