from rest_framework.serializers import ModelSerializer

from apps.library.models import FriendRequest
from apps.user.api.CustomUser.serializer import CustomUserSerializer



class FriendRequestDestroySerializer(ModelSerializer):
    from_user = CustomUserSerializer(read_only=True)
    to_user = CustomUserSerializer(read_only=True)

    class Meta:
        model = FriendRequest
        fields = (
            "id",
            "from_user",
            "to_user",
        )

        extra_kwargs = {
            'id': {'read_only': True}
        }
