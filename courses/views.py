from rest_framework import generics
from .models import Courses
from .serializers import CoursesSerializer, CoursesRetriveSerializer
from rest_framework.authentication import TokenAuthentication
from users.permissions import AdminAuthenticated, StudantAuthenticated
from drf_spectacular.utils import extend_schema
from users.utils import SerializerByMethodMixin


class CoursesListCreateView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [StudantAuthenticated, AdminAuthenticated]
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    
    @extend_schema(description='Lista os cursos criados (Todos os vinculados a algum campus)', tags=['courses'])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @extend_schema(description='Cria um novo curso (Adiministrador ou proprietário)', tags=['courses'])
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class CoursesIdView(SerializerByMethodMixin, generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [StudantAuthenticated, AdminAuthenticated]
    queryset = Courses.objects.all()
    serializer_map = {
        "PATCH": CoursesSerializer,
        "GET": CoursesRetriveSerializer,
        "DELETE": CoursesSerializer,
    }
    
    
    @extend_schema(description='Recupera um curso pelo ID (Todos os vinculados a um campus)', tags=['courses'])
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(description='Atualiza um curso pelo ID (Adiministrador ou proprietário)', tags=['courses'])
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @extend_schema(description='Atualiza parcialmente um curso pelo ID (Adiministrador ou proprietário)', tags=['courses'])
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @extend_schema(description='Deleta um curso pelo ID (Adiministrador ou proprietário)', tags=['courses'])
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)