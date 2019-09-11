from django.urls import path
from . import views

urlpatterns = [
    path('', views.fib_number, name='fib_number'),
]