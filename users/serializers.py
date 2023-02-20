from rest_framework import serializers
from .models import User
from rest_framework.exceptions import PermissionDenied


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'cellphone', 'created_at']
        
    def create(self, validate_data: dict):
        user_authenticate = self.context['request'].user
        users_already_exists = User.objects.all()
        if len(users_already_exists) == 0:
            create_user = User.objects.create_user(**validate_data)
            return create_user
        elif user_authenticate.role.permission >=7:
            create_user = User.objects.create_user(**validate_data)
        else:
            raise PermissionDenied("O usuário não tem permissão para realizar essa ação.") 

    def update(self, instance, validated_data):
        user_authenticate = self.context['request'].user
        pk_params = self.context['view'].kwargs['pk']
        password = validated_data.pop('password', None);

        import ipdb ; ipdb.set_trace()
        if pk_params == str(user_authenticate.id) and password is not None:
            instance.set_password(password)
            instance.save()

        elif user_authenticate.role is True and user_authenticate.role.permission >=7 and password is None:
            User.objects.filter(id=pk_params).update(**self.context['request'].data)
        
        else:
            raise PermissionDenied("O usuário não tem permissão para realizar essa ação.") 
            
        return super().update(instance, validated_data)



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

