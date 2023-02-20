from rest_framework import generics
from .models import Campus, Roles
from .serializers import CampusSerializer, RolesSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from users.permissions import AdminAuthenticated, OwnerAuthenticated, StudantAuthenticated

# Create your views here.
class CampusListCreateView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [StudantAuthenticated, IsAuthenticated]
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer
    
    
class CampusIdView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [StudantAuthenticated, AdminAuthenticated, OwnerAuthenticated]
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer


class RolesListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AdminAuthenticated]
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer
    