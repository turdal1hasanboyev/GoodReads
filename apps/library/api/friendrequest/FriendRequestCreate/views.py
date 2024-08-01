from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status

from apps.library.models import FriendRequest
from apps.library.api.friendrequest.FriendRequestCreate.serializer import FriendRequestCreateSerializer


class FriendRequestCreateView(CreateAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestCreateSerializer

    def post(self, request, *args, **kwargs):
        context = {"user": request.user}
        serializer = self.get_serializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(from_user=self.request.user)
        