from .models import Courses
from classes.models import Classes
from campus.models import Campus
from rest_framework import serializers
from django.forms.models import model_to_dict
from django.db import transaction


class CoursesSerializer(serializers.ModelSerializer):
    campus = serializers.ReadOnlyField()
    class Meta:
        model = Courses
        fields = ['title', 'campus']
    
    def create(self, validated_data):
        kwargs = self.context['request'].parser_context['kwargs']
        campus_id = kwargs['campus_id']
        campus = Campus.objects.get(id=campus_id)
        validated_data['campus'] = campus
        course = super().create(validated_data)
        return model_to_dict(course)

        

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

