from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('led_control.urls')),  # Include URLs from the led_control app
]
