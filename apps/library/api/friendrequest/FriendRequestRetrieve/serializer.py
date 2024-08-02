from rest_framework.serializers import ModelSerializer, SerializerMethodField

from apps.library.models import FriendRequest
from apps.user.api.CustomUser.serializer import CustomUserSerializer
from apps.user.models import User


class FriendRequestSerializer(ModelSerializer):
    to_user = CustomUserSerializer(read_only=True)

    class Meta:
        model = FriendRequest
        fields = (
            "id",
            "to_user"
            "created_at",
        )

        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
        }


class MyFriendsSerializer(ModelSerializer):
    to_users = SerializerMethodField()

    @staticmethod
    def get_to_users(obj):
        print(obj.from_users.all())

        return FriendRequestSerializer(obj.from_users.all(), many=True).data

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "email",
            "to_users",
            "created_at",
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)

        data["friends_count"] = data["to_users"].__len__()

        return data
    