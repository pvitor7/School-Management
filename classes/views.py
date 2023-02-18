from rest_framework import generics
from .models import Classes
from .serializers import ClassesSerializer
# from users.utils import SerializerByMethodMixin


class ClassesListCreateView(generics.ListCreateAPIView):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer
    
    
class ClassesIdView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer
    