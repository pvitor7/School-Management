from .models import Courses
from classes.models import Classes
from rest_framework import serializers
from django.forms.models import model_to_dict

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'
        

class CoursesRetriveSerializer(serializers.ModelSerializer):
    classes = serializers.SerializerMethodField()
    class Meta:
        model = Courses
        fields = "__all__"

    def get_classes(self, obj):
        list_classes = []
        classes = Classes.objects.filter(courses=obj)
        for item in classes:
            classe = model_to_dict(item)
            classe['id'] = str(item.id)
            list_classes.append(classe)
            
        return list_classes

