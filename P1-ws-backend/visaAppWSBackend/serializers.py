from rest_framework import serializers
from .models import Tarjeta, Pago

class TarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjeta  
        fields = ['numero', 'nombre', 'fechaCaducidad', 'codigoAutorizacion']

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'