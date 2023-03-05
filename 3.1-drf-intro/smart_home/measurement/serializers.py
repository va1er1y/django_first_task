from rest_framework import serializers

# TODO: опишите необходимые сериализаторы
from .models import transmitter, temperature_measure


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = temperature_measure
        fields = ['value', 'date']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = transmitter
        fields = ['id', 'name', 'description', 'measurements']