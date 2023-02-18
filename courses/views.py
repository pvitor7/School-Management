from rest_framework import generics
from .models import Courses
from .serializers import CoursesSerializer
from rest_framework.authentication import TokenAuthentication
from users.permissions import AdminAuthenticated, StudantAuthenticated


class CoursesListCreateView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [StudantAuthenticated, AdminAuthenticated]
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    
    
class CoursesIdView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [StudantAuthenticated, AdminAuthenticated]
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    