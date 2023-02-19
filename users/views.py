from django.contrib.auth import authenticate
from .serializers import LoginSerializer, UserSerializer
from rest_framework import generics
from .models import User
from rest_framework.views import Request, Response, APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .utils import SerializerByMethodMixin
from .permissions import AssistantAuthenticated, UserAccountOrAdmin, OwnerAuthenticated, UserAccountOrAassistant

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AssistantAuthenticated, UserAccountOrAdmin]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserIdView(SerializerByMethodMixin, generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_map = {
        'GET': UserSerializer,
        'PATCH': UserSerializer,
        'DELETE': UserSerializer
    }

    
class LoginView(APIView):
    
    def post(self, request: Request) -> Response:
        user_dict = request.data
        serializer = LoginSerializer(data=user_dict)
        serializer.is_valid(raise_exception=True)
        login_user = authenticate(**serializer.validated_data)
        token, _ = Token.objects.get_or_create(user=login_user)
        return Response({"token": token.key})
        