from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from users.permissions import AdminAuthenticated, OwnerAuthenticated, StudantAuthenticated
from drf_spectacular.utils import extend_schema
from users.utils import SerializerByMethodMixin
from .models import Subjects, SubjectsStudants
from .serializers import SubjectsSerializer

class SubjectsListCreateView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [StudantAuthenticated, AdminAuthenticated]
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializer

    @extend_schema(description='Lista os campus criados (Todos os vinculados a algum campus)', tags=['subjects'])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @extend_schema(description='Criação de um novo Campus  (Proprietário, que será o primeiro usuário criado)', tags=['subjects'])
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SubjectsIdView(SerializerByMethodMixin, generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [StudantAuthenticated, AdminAuthenticated, OwnerAuthenticated]
    queryset = Subjects.objects.all()
    serializer_map = {
        "PATCH": SubjectsSerializer,
        "GET": SubjectsSerializer,
        "DELETE": SubjectsSerializer,
    }

    @extend_schema(description='Recuperação de Disciplina (Todos os vinculados a um campus)', tags=['subjects'])
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(description='Atualização de Disciplina (Adiministrador ou proprietário)', tags=['subjects'])
    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @extend_schema(description='Deleção de Disciplina (Proprietário)', tags=['subjects'])
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


