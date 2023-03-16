from .models import Campus, Roles
from rest_framework import serializers
from django.db import transaction
from .utils import roles
from users.models import User
from courses.models import Courses
from django.forms.models import model_to_dict
from django.http import Http404


class CampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campus
        fields = "__all__"

    def create(self, validated_data):
        with transaction.atomic():
            campus_already_exists = Campus.objects.filter(title=validated_data['title'])
            if len(campus_already_exists) < 0:
                raise serializers.ValidationError("Title Campus already exists.")
                
            campus = Campus.objects.create(**validated_data)
            for role in roles:
                Roles.objects.create(title=role['title'], permission=role['permission'], campus=campus)
            
            owner = Roles.objects.get(campus=campus, permission=9)
            User.objects.filter(id=self.context['request'].user.id).update(role=owner)
        return campus


class CampusRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campus
        fields = "__all__"
    courses = serializers.SerializerMethodField()

    def get_courses(self, obj):
        list_courses = []
        courses = Courses.objects.filter(campus=obj)
        for item in courses:
            course = model_to_dict(item)
            course['id'] = str(item.id)
            list_courses.append(course)
        return list_courses



class RolesSerializer(serializers.ModelSerializer):
    campus_name = serializers.SerializerMethodField()
    class Meta:
        model = Roles
        fields = ['id', 'title', 'permission', 'campus', 'campus_name']


    def get_campus_name(self, obj):
        campus_name = Campus.objects.get(id=obj.campus.id).title
        return campus_name
