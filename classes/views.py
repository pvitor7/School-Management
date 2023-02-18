from rest_framework import generics
from .models import Classes
from .serializers import ClassesSerializer
from rest_framework.authentication import TokenAuthentication
from users.permissions import AssistantAuthenticated, AdminAuthenticated


class ClassesListCreateView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AssistantAuthenticated, AdminAuthenticated]
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer
    
    
class ClassesIdView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AssistantAuthenticated, AdminAuthenticated]
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer
    