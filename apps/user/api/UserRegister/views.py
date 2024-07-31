import random

from rest_framework import status
from rest_framework.response import Response

from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny

from apps.user.models import User, VerifyEmail
from apps.user.utils import Util
from apps.user.api.UserRegister.serializer import UserRegisterSerializer


class UserRegisterCreateView(GenericAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            email = request.data.get("email")
            exists_user = User.objects.filter(email=email).first()

            if exists_user and exists_user.is_verified:
                return Response(
                    {"error": "Already registered with this email! Please sign in"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            else:
                code = str(random.randint(100_000, 999_999))
                data = {
                    "to_email": email,
                    "email_subject": "<h1>Check your verifiy code</h1>",
                    "email_body": f"<h2>This is your {code} verifiy code!</h2>"
                }

                Util.send_email(data=data)

                VerifyEmail.objects.create(email=email, code=code)

                serializer = self.serializer_class(data=request.data)
                serializer.is_valid(raise_exception=True)
                
                serializer.save()

                return Response({'success': True, 'message': 'Please verify Email'},
                                status=status.HTTP_201_CREATED)
            
        except Exception as error:
            return Response(
                {
                    "error": f"{error}"
                }, status=status.HTTP_400_BAD_REQUEST
            )
        