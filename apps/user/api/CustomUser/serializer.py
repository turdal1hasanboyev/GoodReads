from rest_framework.serializers import ModelSerializer

from apps.user.models import User


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            "created_at",
        ]
        