from django.urls import path
from . import views

app_name="airbnb"
urlpatterns = [
    path("api/",views.CitiesListView.as_view(),name="airbnb_home"),
    path("api/ciudades/",views.CiudadesListView.as_view(),name="ciudades"),
    path("api/ciudades/<slug:slug>/",views.CiudadesView.as_view(),name="ciudades_items"),
    path("api/<slug:slug>/",views.CitiesView.as_view(),name="cities")
]
