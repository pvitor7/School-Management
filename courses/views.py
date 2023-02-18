from rest_framework import generics
from .models import Courses
from .serializers import CoursesSerializer
# from users.utils import SerializerByMethodMixin


class CoursesListCreateView(generics.ListCreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    
    
class CoursesIdView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    