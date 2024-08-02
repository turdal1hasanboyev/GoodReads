from rest_framework.serializers import ModelSerializer

from apps.library.models import FriendRequest


class FriendRequestDestroySerializer(ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = (
            "id",
            "from_user",
            "to_user",
            "created_at",
        )
