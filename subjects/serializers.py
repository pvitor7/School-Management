from rest_framework import serializers
from .models import Subjects, SubjectsStudants
from users.models import User
from django.db import transaction
from classes.models import Classes
from courses.models import Courses
from courses.serializers import CoursesSerializer


class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = ['title']
         
    def create(self, validated_data: dict):
        with transaction.atomic():
            course = self.context['request'].parser_context['kwargs']['course_id']
            validated_data['course'] = Courses.objects.get(id=course)
            #criando a disciplina
            new_subject = Subjects.objects.create(**validated_data);
            #criando na tabela pivo
            #pegando todas as turmas do curso
            list_classes = Classes.objects.filter(courses=course)
            
            for item in list_classes:
                #pegando todos os usuários associados as classes dos cursos e atualizando com a conexão da tabela pivô
                list_studant = User.objects.filter(classe=item)
                
                for user in list_studant:
                    SubjectsStudants.objects.create(subject=new_subject, user=user);
                                            
        return new_subject;
