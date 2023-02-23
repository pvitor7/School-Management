from rest_framework import serializers
from .models import Subjects, SubjectsStudants
from users.models import User
from django.db import transaction
from classes.models import Classes


class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = '__all__'
        
        
    def create(self, validate_data: dict):
        with transaction.atomic():
            #criando a disciplina
            new_subject = Subjects.objects.create(**validate_data);
            #criando a tabela pivo
            subject_studant = SubjectsStudants.objects.create(subject=new_subject);
            #pegando todas as turmas do curso
            list_classes = Classes.objects.filter(course=validate_data['course'])
            
            for item in list_classes:
                #pegando todos os usuários associados as classes dos cursos e atualizando com a conexão da tabela pivô
                User.objects.filter(classe=item).update(subject=subject_studant);
                        
        return new_subject;
    