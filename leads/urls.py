from django.urls import path, reverse
from .views import *


urlpatterns = [
    path('', home, name='index'),
    path('consulta2/', UniEconomicaListView.as_view(), name='uniEconomicas-list'),
    path('obtener-unidades/', obtener_unidades, name='obtener-unidades'),
    path('obtener-condiciones/',obtener_condiciones, name='obtener-condiciones'),
    path('obtener-filtros/', obtener_filtros, name='obtener-filtros'),
    path('obtener-municipios/', obtener_municipios, name='obtener_municipios'),
    path('obtener-localidades/', obtener_localidades, name='obtener_localidades'),
    path('consultar-datos/', consultar_datos, name='consultar_datos')
]