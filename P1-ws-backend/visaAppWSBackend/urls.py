"""
URL configuration for PagoProj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from visaAppWSBackend.views import (TarjetaView, PagoView,
                           ComercioView)
"""
urlpatterns = [
    path("", aportarinfo_tarjeta, name="index"),
    path("tarjeta/", aportarinfo_tarjeta, name="tarjeta"),
    path("pago/", aportarinfo_pago, name="pago"),
    path("testbd/", testbd, name="testbd"),
    path("testbd/getpagos/", getpagos, name="getpagos"),
    path("testbd/delpago/", delpago, name="delpago"),
]
"""

urlpatterns = [
    # check if tarjeta is in " tarjeta "
    path('tarjeta/', TarjetaView.as_view() ,name='tarjeta'),
    # create " pago "
    path('pago/', PagoView.as_view() , name='pago'),
    # get list of " pagos " associated with a given idComercio
    path('comercio/<str:idComercio>/', ComercioView.as_view() , name='comercio'),
    # delete " pago " with id id_pago
    path('pago/<str:id_pago>/', PagoView.as_view(), name='pago') ,
]
