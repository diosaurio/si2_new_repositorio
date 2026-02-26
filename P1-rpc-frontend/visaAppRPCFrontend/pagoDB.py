# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# author: rmarabini
"Interface with the dataabse"
from django.conf import settings
from xmlrpc.client import ServerProxy


def verificar_tarjeta(tarjeta_data):
    """ Check if the tarjeta is registered 
    :param tarjeta_dict: dictionary with the tarjeta data
    :return True or False if tarjeta_data is not valid
    """
    with ServerProxy(settings.RPCAPIBASEURL) as proxy:
        return proxy.verificar_tarjeta(tarjeta_data)


def registrar_pago(pago_dict):
    """ Register a payment in the database
    :param pago_dict: dictionary with the pago data
      plus de tarjeta_id (numero) of the tarjeta
    :return new pago info dictionary with the time
    """
    with ServerProxy(settings.RPCAPIBASEURL) as proxy:
        return proxy.registrar_pago(pago_dict)


def eliminar_pago(idPago):
    """ Delete a pago in the database
    :param idPago: id of the pago to be deleted
    :return True if succesful,
     False otherwise
     """
    with ServerProxy(settings.RPCAPIBASEURL) as proxy:
        return proxy.eliminar_pago(idPago)


def get_pagos_from_db(idComercio):
    """ Gets pagos in the database correspondint to some idComercio
    :param idComercio: id of the comercio to get pagos from 
    :return list of pagos in dictionary found
     """
    with ServerProxy(settings.RPCAPIBASEURL) as proxy:
        return proxy.get_pagos_from_db(idComercio)
