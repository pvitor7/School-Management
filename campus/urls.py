from .views import CampusListCreateView, CampusIdView, RolesListView
from django.urls import path

urlpatterns = [
    path("", CampusListCreateView.as_view(), name="campus-list-create-view"),
    path("roles/", RolesListView.as_view(), name="list-roles-view"),
    path("<pk>/", CampusIdView.as_view(), name="campus-retrive-view"),
]   