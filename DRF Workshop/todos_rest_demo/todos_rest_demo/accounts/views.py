from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.authtoken import views as auth_views
from rest_framework import generics as api_views, serializers
from rest_framework.response import Response

# Create your views here.
UserModel = get_user_model()


class ApiLoginView(auth_views.ObtainAuthToken):
    pass


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'password')

    # Model -> JSON, called on '.data', NO SAVING
    # 1.
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop('password')
        return data

    # 2.
    def save(self, **kwargs):
        user = super().save(**kwargs)

        user.set_password(user.password)
        user.save()

        return user

    def validate(self, attrs):
        password = attrs.get('password', None)
        try:
            validate_password(password)
            return attrs
        finally:
            return attrs

    # JSON -> Model
    # def to_internal_value(self, data):
    #     pass

    # 1. Password is returned as a response.
    # 2. Password is saved as plain text.
    # 3. Password validators don't work


class ApiRegisterView(api_views.CreateAPIView):
    serializer_class = RegisterUserSerializer


class ApiLogoutView(api_views.views.APIView):
    def post(self, request, *args, **kwargs):
        return self.__perform_logout(request)

    def get(self, request, *args, **kwargs):
        return self.__perform_logout(request)

    @staticmethod
    def __perform_logout(request):
        request.user.auth_token.delete()
        return Response({
            'message': 'user logged out'
        })
