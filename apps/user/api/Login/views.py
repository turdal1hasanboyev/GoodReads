from rest_framework.permissions import AllowAny

from rest_framework_simplejwt.views import TokenObtainPairView

from apps.user.api.Login.serializer import CustomTokenObtainPairSerializer


class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = [AllowAny]
    