from rest_framework.serializers import ModelSerializer, ValidationError

from apps.library.models import FriendRequest


class FriendRequestCreateSerializer(ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = (
            "id",
            "from_user",
            "to_user",
            "created_at",
        )

        extra_kwargs = {
            "id": {"read_only": True},
            "from_user": {"read_only": True},
        }

    def validate(self, attrs):
        user_id = self.context["user"].id

        if user_id == attrs["to_user"].id:
            print("You can't send friend request to yourself")

            raise ValidationError({"error": "You can't send friend request to yourself"})

        exists_friend_request = FriendRequest.objects.filter(
            from_user_id=user_id, to_user_id=attrs["to_user"].id
        ).values_list("id", flat=True).exists()

        if exists_friend_request:
            raise ValidationError({"error": "You have already sent friend request to this user"})

        return attrs
    