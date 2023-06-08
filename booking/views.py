from django.shortcuts import render

from rest_framework import generics
from .models import Service
from .seriealizers import ServiceSerializer
# Create your views here.


class ServiceTypes(generics.ListCreateAPIView):
   
    serializer_class = ServiceSerializer
    name = 'service'
    
    def get_queryset(self):
        queryset = Service.objects.all()
        start_from = self.request.query_params.get('start_from')
        ends_at = self.request.query_params.get('ends_at')

        if start_from and ends_at:
            queryset = queryset.filter(start_from=start_from, ends_at=ends_at)

        return queryset