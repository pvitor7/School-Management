from .models import Campus, Roles
from rest_framework import serializers
from django.db import transaction
from .utils import roles
from users.models import User


class CampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campus
        fields = "__all__"

    def create(self, validated_data):
        with transaction.atomic():
            campus = Campus.objects.create(**validated_data)
            
            for role in roles:
                Roles.objects.create(title=role['title'], permission=role['permission'], campus=campus)
            
            owner = Roles.objects.get(campus=campus, permission=9)
            User.objects.filter(id=self.context['request'].user.id).update(role=owner)
        return campus


class RolesSerializer(serializers.ModelSerializer):
    campus_name = serializers.SerializerMethodField()
    class Meta:
        model = Roles
        fields = ['id', 'title', 'permission', 'campus', 'campus_name']


    def get_campus_name(self, obj):
        campus_name = Campus.objects.get(id=obj.campus.id).title
        return campus_name
