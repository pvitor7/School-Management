from rest_framework import generics
from .models import Campus, Roles
from .serializers import CampusSerializer, RolesSerializer, CampusRetriveSerializer
from rest_framework.authentication import TokenAuthentication
from users.permissions import AdminAuthenticated, OwnerAuthenticated, StudantAuthenticated
from drf_spectacular.utils import extend_schema
from users.utils import SerializerByMethodMixin

class CampusListCreateView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [StudantAuthenticated, AdminAuthenticated]
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer

    @extend_schema(description='Lista os campus criados (Todos os vinculados a algum campus)', tags=['campus'])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @extend_schema(description='Criação de um novo Campus  (Proprietário, que será o primeiro usuário criado)', tags=['campus'])
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CampusIdView(SerializerByMethodMixin, generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [StudantAuthenticated, AdminAuthenticated, OwnerAuthenticated]
    queryset = Campus.objects.all()
    serializer_map = {
        "PATCH": CampusSerializer,
        "GET": CampusRetriveSerializer,
        "DELETE": CampusRetriveSerializer,
    }

    @extend_schema(description='Recuperação de Campus (Todos os vinculados a um campus)', tags=['campus'])
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(description='Atualização de Campus (Adiministrador ou proprietário)', tags=['campus'])
    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @extend_schema(description='Atualização de Campus (Adiministrador ou proprietário)', tags=['campus'])
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @extend_schema(description='Deleção de Campus (Proprietário)', tags=['campus'])
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class RolesListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AdminAuthenticated]
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer
    
    @extend_schema(description='Recuperação de Roles para inclusão de IDs na criação de usuários (Administrador ou proprietário)', tags=['roles'])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
