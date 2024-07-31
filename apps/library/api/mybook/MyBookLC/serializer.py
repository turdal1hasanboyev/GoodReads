from rest_framework.serializers import ModelSerializer

from apps.library.models import MyBook


class MyBookLCSerializer(ModelSerializer):
    class Meta:
        model = MyBook
        fields = (
            'id',
            "user",
            'book',
            'date_read',
        )

        extra_kwargs = {
            "id": {"read_only": True},
        }
        