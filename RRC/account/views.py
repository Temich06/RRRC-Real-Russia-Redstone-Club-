from knox.models import AuthToken
from account.serializers import UserSerializer, RegisterSerializer
from rest_framework.response import Response
from knox.views import LoginView as KnoxLoginView
from knox.views import LogoutView as KnoxLogoutView
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login, logout
from rest_framework import generics


# Create your views here.


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


class RegisterAPI(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LogoutAPI(KnoxLogoutView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        logout(request)
        return Response({

        })