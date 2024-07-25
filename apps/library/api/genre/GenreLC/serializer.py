from rest_framework.serializers import ModelSerializer

from apps.library.models import Genre


class GenreLCSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = (
            'id',
            "name",
            'parent',
        )

        extra_kwargs = {
            "id": {"read_only": True},
        }
        