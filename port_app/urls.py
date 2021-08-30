from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('portal', views.portal),
]