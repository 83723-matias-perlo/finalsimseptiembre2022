'''Modulo de servidores, incluye funciones de gets'''

from Negocio.Cola import Cola


def getEncargado(colaTurno: Cola, colaTarifa: Cola):
    from .Encargado import Encargado
    return Encargado(colaTurno, colaTarifa)

def getMozo():
    from .Mozo import Mozo
    return Mozo()

def getTerminal():
    from .Terminal import Terminal
    return Terminal()

def getImpresora():
    from .Impresora import Impresora
    return Impresora()