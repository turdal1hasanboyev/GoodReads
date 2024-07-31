from rest_framework.generics import DestroyAPIView
from rest_framework.serializers import ValidationError

from apps.library.models import FriendRequest

from apps.library.api.friendrequest.FriendRequestDestroy.serializer import FriendRequestDestroySerializer


class FriendRequestDestroyView(DestroyAPIView):
    serializer_class = FriendRequestDestroySerializer
    queryset = FriendRequest.objects.all()
    lookup_field = "pk"

    def perform_destroy(self, instance):
        print(instance.from_user, self.request.user)
        
        if self.request.user.id == instance.from_user.id:
            instance.delete()
        else:
            raise ValidationError("You are not allowed to delete this friend request")
        