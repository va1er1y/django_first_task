# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from django.forms import  model_to_dict
# from smart_home.measurement.models import transmitter, temperature_measure
# from smart_home.measurement.serializers import MeasurementSerializer, SensorDetailSerializer
# smart_home.measurement
from .models import transmitter, temperature_measure
from .serializers import MeasurementSerializer, SensorDetailSerializer


class sensor(ListAPIView):
    # queryset = transmitter.objects.all()
    # serializer_class = SensorDetailSerializer

    # def post(self, request):
    #     sensor = request.GET.get("sensor")
    #     descriptions = request.GET.get("description")
    #     # add_sensor = transmitter(name=sensor, description=descriptions)
    #     # add_sensor.save()
    #     transmitter.objects.create(name=sensor, description=descriptions)
    #     return Response({'status': 'ADD'})
        # return Response('status':'')

    def post(self, request):
        add_sensor = transmitter.objects.create(
            name=request.data['name'],
            description=request.data['description'])
        return Response({'status': model_to_dict(add_sensor)})

    def patch(self, request):
        name = request.data['name'],
        description = request.data['description']
        if name and description is not None:
            change_sensor = transmitter.objects.create(name, description)
            return Response({'status': model_to_dict(change_sensor)})
        if (name is not None) and (description is None):
            change_sensor = transmitter.objects.create(name)
            return Response({'status': model_to_dict(change_sensor)})
        else:
            change_sensor = transmitter.objects.create(description)
            return Response({'status': model_to_dict(change_sensor)})

            # def get(self, request):
    #     queryset = transmitter.objects.all()
    #     return Response(queryset)

class measure(RetrieveAPIView):
    queryset = temperature_measure.objects.all()
    serializer_class = SensorDetailSerializer