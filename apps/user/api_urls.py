from django.urls import path

from .api.UserRegister.views import UserRegisterCreateView
from .api.EmailVerify.views import EmailVerifyGenericView


app_name = "user"

urlpatterns = [
    path('register/', UserRegisterCreateView.as_view(), name="register"),
    path('verify/', EmailVerifyGenericView.as_view(), name="user_verify"),
]
