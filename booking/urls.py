from django.urls import path
from .views import ServiceTypes

urlpatterns = [
    path('search/',ServiceTypes.as_view(),name = ServiceTypes.name)
]
