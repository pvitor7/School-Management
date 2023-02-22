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
            studant = {"id": item.id, "first_name": item.first_name, "last_name": item.last_name, "cellphone": item.cellphone, "email": item.email}
            list_classes.append(studant)
        return list_classes

