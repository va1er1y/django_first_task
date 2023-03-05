from django.urls import path

# from measurement.views import measure, sensor
# from . import views
from .views import measure, sensor

urlpatterns = [
         path('sensors/', sensor.as_view()),
]
