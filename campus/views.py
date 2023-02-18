from rest_framework import generics
from .models import Campus
from .serializers import CampusSerializer
from users.utils import SerializerByMethodMixin

# Create your views here.
class CampusListCreateView(generics.ListCreateAPIView):
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer
    
    
class CampusIdView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer
    