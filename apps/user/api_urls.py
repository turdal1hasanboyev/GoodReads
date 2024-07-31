from django.urls import path

from apps.user.api.UserRegister.views import UserRegisterCreateView

from apps.user.api.EmailVerify.views import EmailVerifyGenericView


app_name = "user"

urlpatterns = [
    path('register/', UserRegisterCreateView.as_view(), name="register"),
    path('verify/', EmailVerifyGenericView.as_view(), name="user_verify"),
]
