from django.urls import path

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer
from measurement.views import Sensors, Measurements, UpdateSensor, SensorDetail

urlpatterns = [
    # Создание датчика.
    # Получить список датчиков.
    path('sensors/', Sensors.as_view()),
    # изменение датчика
    path('sensors/<int:pk>/', UpdateSensor.as_view()),
    # Добавить измерение.
    path('measurements/<sensor>/', Measurements.as_view()),
    # Получить информацию по конкретному датчику.
    path('sensor/<int:pk>/', SensorDetail.as_view())
]
