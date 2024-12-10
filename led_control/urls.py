from django.urls import path
from . import views

urlpatterns = [
    path('', views.led_control, name='led_control'),
    path('control/<str:action>/', views.control_led, name='control_led'),
]
