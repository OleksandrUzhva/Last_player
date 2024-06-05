from rest_framework import generics, permissions, serializers, status
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "login",
            "email",
            "password",
            "positions",
            "is_active",
        ]  # noqa


    def validate(self, attrs):
        attrs["password"] = make_password(attrs["password"])
        return attrs
    
class UserRegistrationPublickSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "login", "email", "positions"]

class UserAPI(generics.ListCreateAPIView):
    http_method_names = ["get", "post"]
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return User.objects.all()

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(
            UserRegistrationPublickSerializer(serializer.data).data,
            status=status.HTTP_201_CREATED,
            headers=self.get_success_headers(serializer.data),
        )
    
    def get(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )
    