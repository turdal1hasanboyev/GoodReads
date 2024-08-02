from rest_framework.serializers import ModelSerializer

from apps.library.models import Award


class AwardLCSerializer(ModelSerializer):
    class Meta:
        model = Award
        fields = (
            'id',
            "name",
            'date',
            "created_at",
        )

        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
        }
        