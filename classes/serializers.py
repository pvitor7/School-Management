from .models import Classes
from rest_framework import serializers


class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = '__all__'
        
   