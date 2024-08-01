from rest_framework import serializers

from apps.user.models import VerifyEmail


class EmailVerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = VerifyEmail
        fields = (
            "email",
            "code",
        )
