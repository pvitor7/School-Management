from .models import Classes
from courses.models import Courses
from courses.serializers import CoursesSerializer
from rest_framework import serializers
from users.models import User
from django.forms.models import model_to_dict
from django.db import transaction


class ClassesSerializer(serializers.ModelSerializer):
    courses = serializers.ReadOnlyField()
    class Meta:
        model = Classes
        fields = ['id', 'title', 'courses']
        
    def create(self, validated_data):
        with transaction.atomic():
            course_id = self.context['request'].parser_context['kwargs']['course_id']
            course = Courses.objects.get(id=course_id)
            validated_data['courses'] = course
            classe = super().create(validated_data)
            classe_id = classe.id
            classe_dict = model_to_dict(classe)
            classe_dict['id'] = classe_id
        return classe_dict
   
   
class ClassesRetriveSerializer(serializers.ModelSerializer):
    studants = serializers.SerializerMethodField()
    class Meta:
        model = Classes
        fields = "__all__"

    def get_studants(self, obj):
        list_classes = []
        classes = User.objects.filter(classe=obj.id)
        for item in classes:
            studant = {"id": item.id, "first_name": item.first_name, "last_name": item.last_name, "cellphone": item.cellphone, "email": item.email}
            list_classes.append(studant)
        return list_classes

