from django.contrib.auth import authenticate
from .serializers import LoginSerializer, UserSerializer
from rest_framework import generics
from .models import User
from django.shortcuts import get_object_or_404
from rest_framework.views import Request, Response, APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from .utils import SerializerByMethodMixin
from .permissions import AssistantAuthenticated, UserAccountOrAdmin, UserAccountOrAassistant
from drf_spectacular.utils import extend_schema

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @extend_schema(description='Cria um novo usuário (Sem autenticação apenas para o primeiro usuário)', tags=['users'])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AssistantAuthenticated, UserAccountOrAdmin]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @extend_schema(description='Lista todos os usuários', tags=['users'])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    

class UserIdView(SerializerByMethodMixin, generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserAccountOrAassistant, UserAccountOrAdmin]
    queryset = User.objects.all()
    serializer_map = {
        'GET': UserSerializer,
        'PATCH': UserSerializer,
        'DELETE': UserSerializer
    }
    
    @extend_schema(description='Recupera um usuário pelo ID', tags=['users'])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(description='Atualiza um usuário pelo ID', tags=['users'])
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(description='Atualiza parcialmente um usuário pelo ID', tags=['users'])
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(description='Deleta um usuário pelo ID', tags=['users'])
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    

    
class LoginView(APIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    
    @extend_schema(description='Login de usuários')
    def post(self, request: Request) -> Response:
        user_dict = request.data
        
        if request.data.get('email'):
            username = get_object_or_404(
            User, email=request.data['email']).username
            user_dict['username'] = username

        elif request.data.get('cellphone'):
            username = get_object_or_404(
            User, cellphone=request.data['cellphone']).username
            user_dict['username'] = username
        
        serializer = LoginSerializer(data=user_dict)
        serializer.is_valid(raise_exception=True)
        login_user = authenticate(**serializer.validated_data)
        token, _ = Token.objects.get_or_create(user=login_user)
        return Response({"token": token.key})
        