from rest_framework.generics import DestroyAPIView
from rest_framework.serializers import ValidationError

from apps.library.models import FriendRequest
from .serializer import FriendRequestDestroySerializer


class FriendRequestDestroyView(DestroyAPIView):
    serializer_class = FriendRequestDestroySerializer
    queryset = FriendRequest.objects.all()
    lookup_field = "pk"

    def perform_destroy(self, instance):        
        if self.request.user.id == instance.from_user.id:
            instance.delete()

        else:
            raise ValidationError("You are not allowed to delete this friend request")
        