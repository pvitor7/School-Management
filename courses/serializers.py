from .models import Courses
from rest_framework import serializers


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'
        
   