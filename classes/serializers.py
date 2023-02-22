from .models import Classes
from rest_framework import serializers
from users.models import User
from django.forms.models import model_to_dict


class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = '__all__'
        
   
class ClassesRetriveSerializer(serializers.ModelSerializer):
    studants = serializers.SerializerMethodField()
    class Meta:
        model = Classes
        fields = "__all__"

    def get_studants(self, obj):
        list_classes = []
        classes = User.objects.filter(classe=obj.id)
        for item in classes:
            list_classes.append(model_to_dict(item))
        return list_classes

