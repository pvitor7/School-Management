from rest_framework import generics
from .models import Campus
from .serializers import CampusSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from users.permissions import UserAuthenticated

# Create your views here.
class CampusListCreateView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer
    
    
class CampusIdView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, UserAuthenticated]
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer
    