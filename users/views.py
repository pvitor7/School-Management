from django.contrib.auth import authenticate
from .serializers import LoginSerializer, UserSerializer
from rest_framework import generics
from .models import User
from rest_framework.views import Request, Response, APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .utils import SerializerByMethodMixin
from .permissions import AssistantAuthenticated, UserAccountOrAdmin
from drf_spectacular.utils import extend_schema

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @extend_schema(description='Cria um novo usuário', tags=['usuários'])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AssistantAuthenticated, UserAccountOrAdmin]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @extend_schema(description='Lista todos os usuários', tags=['usuários'])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    

class UserIdView(SerializerByMethodMixin, generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_map = {
        'GET': UserSerializer,
        'PATCH': UserSerializer,
        'DELETE': UserSerializer
    }
    
    @extend_schema(description='Recupera um usuário pelo ID', tags=['usuários'])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(description='Atualiza um usuário pelo ID', tags=['usuários'])
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(description='Atualiza parcialmente um usuário pelo ID', tags=['usuários'])
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(description='Deleta um usuário pelo ID', tags=['usuários'])
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    

    
class LoginView(APIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    @extend_schema(description='Login de usuários', tags=['usuários'])
    def post(self, request: Request) -> Response:
        user_dict = request.data
        serializer = LoginSerializer(data=user_dict)
        serializer.is_valid(raise_exception=True)
        login_user = authenticate(**serializer.validated_data)
        token, _ = Token.objects.get_or_create(user=login_user)
        return Response({"token": token.key})
        