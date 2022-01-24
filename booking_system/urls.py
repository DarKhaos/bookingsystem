"""booking_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from booking.views import CustomerAPIView, RoomAPIView, BookingAPIView, PaymentAPIView

API_PATH = 'api'
API_VERSION = 'v1'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path(f'{API_PATH}/{API_VERSION}/customers/', CustomerAPIView.as_view()),
    path(f'{API_PATH}/{API_VERSION}/customers/<int:pk>/', CustomerAPIView.as_view()),
    path(f'{API_PATH}/{API_VERSION}/rooms/', RoomAPIView.as_view()),
    path(f'{API_PATH}/{API_VERSION}/rooms/<int:pk>/', RoomAPIView.as_view()),
    path(f'{API_PATH}/{API_VERSION}/bookings/', BookingAPIView.as_view()),
    path(f'{API_PATH}/{API_VERSION}/bookings/<int:pk>/', BookingAPIView.as_view()),
    path(f'{API_PATH}/{API_VERSION}/bookings/<int:pk>/payments/', PaymentAPIView.as_view()),
    path(f'{API_PATH}/{API_VERSION}/bookings/<int:pk>/payments/<int:ppk>/', PaymentAPIView.as_view())
]
