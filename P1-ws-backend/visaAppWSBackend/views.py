from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TarjetaSerializer, PagoSerializer
from .models import Tarjeta, Pago
from rest_framework import status
from django.http import Http404
from .pagoDB import (verificar_tarjeta, registrar_pago, eliminar_pago, get_pagos_from_db)

class TarjetaView(APIView):
    def post(self, request):
        if verificar_tarjeta(request.data):
            return Response({'message': 'Datos encontrados en la base de datos'}, status=status.HTTP_200_OK)
        return Response({'message': 'Datos no encontrados en la base de datos'}, status=status.HTTP_404_NOT_FOUND)
          

class PagoView(APIView):
    def post(self, request):
        pago = registrar_pago(request.data)
        if pago:
            return Response(PagoSerializer(pago).data, status=status.HTTP_200_OK)
        return Response({'message': 'Error al registrar pago.'}, status=status.HTTP_404_NOT_FOUND)

    
    def delete(self, request, **kwargs):
        id_pago = kwargs.get('id_pago', None)

        if not id_pago:
            return Response({'message':'Falta el id de pago.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not eliminar_pago(id_pago):
            return Response({'message': 'Pago no encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        
        return Response({'message': 'Pago borrado correctamente.'}, status=status.HTTP_200_OK)
    
class ComercioView(APIView):
    def get(self, request, **kwargs):
        id_comercio = kwargs.get('idComercio', None)

        if not id_comercio:
            return Response({'message':'Falta el id de comercio.'}, status=status.HTTP_400_BAD_REQUEST)
        
        pagos = get_pagos_from_db(id_comercio)

        if not pagos:
            return Response([], status=status.HTTP_200_OK)
        
        return Response(PagoSerializer(pagos, many=True).data, status=status.HTTP_200_OK)