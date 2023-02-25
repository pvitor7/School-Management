from .views import CampusListCreateView, CampusIdView, RolesListView
from django.urls import path

urlpatterns = [
    path("", CampusListCreateView.as_view()),
    path("roles/", RolesListView.as_view()),
    path("<pk>/", CampusIdView.as_view()),
    
]   