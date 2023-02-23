from .models import Courses
from classes.models import Classes
from campus.models import Campus
from campus.serializers import CampusSerializer
from rest_framework import serializers
from django.forms.models import model_to_dict
from django.db import transaction


class CoursesSerializer(serializers.ModelSerializer):
    campus = CampusSerializer(read_only=True)
    class Meta:
        model = Courses
        fields = ['id', 'title', 'campus']
    
    def create(self, validated_data):
        with transaction.atomic():
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

    def to_representation(self, instance):
        kwargs = self.context['request'].parser_context['kwargs']
        campus_id = kwargs['campus_id']
        course_id = kwargs['pk']
        course = Courses.objects.get(id=course_id, campus=campus_id)
        return super().to_representation(course)


class CreateCoursesSerializer(serializers.ModelSerializer):
    campus = serializers.ReadOnlyField()
    class Meta:
        model = Courses
        fields = ['id', 'title', 'campus']
    
    def create(self, validated_data):
        with transaction.atomic():
            campus_id = self.context['request'].parser_context['kwargs']['campus_id']
            campus = Campus.objects.get(id=campus_id)
            validated_data['campus'] = campus
            course = super().create(validated_data)
            course_id = course.id
            course_dict = model_to_dict(course)
            course_dict['id'] = course_id
        return course_dict