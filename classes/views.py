from rest_framework import generics
from .models import Classes
from .serializers import ClassesSerializer, ClassesRetriveSerializer
from rest_framework.authentication import TokenAuthentication
from users.permissions import AssistantAuthenticated, AdminAuthenticated
from drf_spectacular.utils import extend_schema

from users.utils import SerializerByMethodMixin

class ClassesListCreateView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AssistantAuthenticated, AdminAuthenticated]
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer
    
    @extend_schema(description='Lista as turmas criadas (Todas as vinculadas a algum curso)', tags=['classes'])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @extend_schema(description='Cria uma nova turma (Adiministrador ou proprietário)', tags=['classes'])
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    
    
class ClassesIdView(SerializerByMethodMixin, generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AssistantAuthenticated, AdminAuthenticated]
    queryset = Classes.objects.all()
    serializer_map = {
        "PATCH": ClassesSerializer,
        "GET": ClassesRetriveSerializer,
        "DELETE": ClassesSerializer,
    }
    
    
    @extend_schema(description='Recupera uma turma pelo ID (Todas as vinculadas a um curso)', tags=['classes'])
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(description='Atualiza uma turma pelo ID (Adiministrador ou proprietário)', tags=['classes'])
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @extend_schema(description='Atualiza parcialmente uma turma pelo ID (Adiministrador ou proprietário)', tags=['classes'])
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @extend_schema(description='Deleta uma turma pelo ID (Adiministrador ou proprietário)', tags=['classes'])
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


