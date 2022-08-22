from typing import List

from .Evento import Evento

def getEventos() -> List[Evento]:
    # import eventos
    from .AsignacionTerminal import AsignacionTerminal
    from .CobroTarifa import CobroTarifa
    from .LlegadaCliente import LlegadaCliente
    from .Navegacion import Navegacion
    from .PedidoBar import PedidoBar
    from .RetiroImpresion import RetiroImpresion

    # import servidores
    from ..Servidores import getEncargado, getImpresora, getMozo, getTerminal

    # import colas
    from ..Cola import Cola

    # colas
    colaEsperaTurno: Cola = Cola()
    colaNavegacion: Cola = Cola()
    colaEsperaMozo: Cola = Cola()
    colaPagoTarifa: Cola = Cola()
    colaRetiroImpresion: Cola = Cola()

    # servidores
    encargado = getEncargado(colaEsperaTurno, colaPagoTarifa)
    mozo = getMozo()
    impresora = getImpresora()
    terminal1 = getTerminal()
    terminal2 = getTerminal()
    terminal3 = getTerminal()

    #eventos
    eventos: List[Evento] = []
    
    eventos.append(LlegadaCliente(None, None, colaEsperaTurno))
    eventos.append(AsignacionTerminal(encargado, colaEsperaTurno, colaNavegacion, colaEsperaMozo))
    eventos.append(PedidoBar(mozo, colaEsperaMozo, None))
    eventos.append(Navegacion(terminal1, colaNavegacion, colaPagoTarifa))
    eventos.append(Navegacion(terminal2, colaNavegacion, colaPagoTarifa))
    eventos.append(Navegacion(terminal3, colaNavegacion, colaPagoTarifa))
    eventos.append(CobroTarifa(encargado, colaPagoTarifa, colaRetiroImpresion))
    eventos.append(RetiroImpresion(impresora, colaRetiroImpresion, None))

    return eventos


    