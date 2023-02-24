from rest_framework import serializers
from .models import User
from campus.models import Roles
from rest_framework.exceptions import PermissionDenied
from subjects.models import SubjectsStudants, Subjects
from django.db import transaction


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'cellphone', 'classe', 'created_at', 'role']
        
    def create(self, validate_data: dict):
        with transaction.atomic():
            user_authenticate = self.context['request'].user
            users_already_exists = User.objects.all()
            new_user_role = validate_data.get('role', None)
            permission = Roles.objects.get(id=new_user_role.id).permission if new_user_role else None
            classe = validate_data.get('classe', None)

            if len(users_already_exists) == 0:
                create_user = User.objects.create_user(**validate_data)
                return create_user

            elif len(users_already_exists) != 0 and new_user_role is None:
                raise PermissionDenied("Propriedade 'role' ausente!")

            elif user_authenticate.role.permission >= 7:
                if permission == 1 and classe is None:
                    raise PermissionDenied("Propriedade 'classe' ausente.")
                create_user = User.objects.create_user(**validate_data)

                if classe:
                    list_subjects = Subjects.objects.filter(course_id=classe.courses.id)
                    for item in list_subjects:
                        SubjectsStudants.objects.create(subject=item, user=create_user)
                return create_user

            else:
                raise PermissionDenied("O usuário não tem permissão para realizar essa ação.")
        

    def update(self, instance, validated_data):
        user_authenticate = self.context['request'].user
        pk_params = self.context['view'].kwargs['pk']
        password = validated_data.pop('password', None);
        if pk_params == str(user_authenticate.id) and password is not None:
            instance.set_password(password)
            instance.save()

        elif user_authenticate.role.permission >=7 and password is None:
            User.objects.filter(id=pk_params).update(**self.context['request'].data)
        
        else:
            raise PermissionDenied("O usuário não tem permissão para realizar essa ação.") 
            
        return super().update(instance, validated_data)



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

