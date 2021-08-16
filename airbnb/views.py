from django.shortcuts import render
from .serializer import CiudadesSerializer,CitiesSerializer
from rest_framework import generics
from .models import Ciudades,Cities
from . import models

class CitiesListView(generics.ListAPIView):
    queryset=Cities.objects.all()
    serializer_class=CitiesSerializer

class CitiesView(generics.RetrieveAPIView):
    lookup_field=['slug']
    queryset=Cities.objects.all()
    serializer_class=CitiesSerializer


class CiudadesView(generics.RetrieveAPIView):
    serializer_class=CitiesSerializer

    def get_queryset(self):
        return models.Cities.objects.filter(
            ciudades__in=Ciudades.objects.get(slug=self.kwargs["slug"]).get_descendants(include_self=True)
        )
class CiudadesListView(generics.ListAPIView):
    queryset=Ciudades.objects.filter(level=1)
    serializer_class=CiudadesSerializer