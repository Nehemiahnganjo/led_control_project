from django.urls import path
from . import views

urlpatterns = [
    path('led/<str:action>/', views.control_led, name='control_led'),  # For 'on'/'off' actions
    path('', views.led_control, name='led_control'),                  # Main control page
]
