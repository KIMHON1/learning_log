from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('article/<int:id>', views.show),
]