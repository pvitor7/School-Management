from .views import CampusListCreateView, CampusIdView
from django.urls import path

urlpatterns = [
    path("", CampusListCreateView.as_view()),
    path("<pk>/", CampusIdView.as_view()),
    
]   