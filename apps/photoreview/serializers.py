from rest_framework import serializers
from apps.photoreview.models import StormTrooper


class StormTrooperSerializer(serializers.ModelSerializer):
    class Meta:
        model = StormTrooper
        fields = [
            'id',
            'name',
            'location'
        ]
