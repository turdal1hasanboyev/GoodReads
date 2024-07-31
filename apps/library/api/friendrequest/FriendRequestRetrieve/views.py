from rest_framework.generics import RetrieveAPIView

from apps.user.models import User
from apps.library.api.friendrequest.FriendRequestRetrieve.serializer import MyFriendsSerializer


class MyFriendsView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = MyFriendsSerializer
    pagination_class = None
    lookup_field = None

    def get_object(self):
        user_id = self.request.query_params.get("user_id")

        if not user_id:
            return User.objects.filter(pk=self.request.user.id, is_verified=True).first()
        
        return User.objects.filter(pk=user_id).first()
    