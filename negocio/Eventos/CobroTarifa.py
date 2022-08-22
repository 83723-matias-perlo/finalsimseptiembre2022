from .Evento import Evento
from ..Cliente import Cliente
from ..Cola import Cola
from ..Servidores.Servidor import Servidor

class CobroTarifa(Evento):
    #static
    __totalGastoAC: float = 0
    __totalClientesPagaron: int = 0

    def getTotalGastoAC():
        return CobroTarifa.__totalGastoAC
    
    def getClientesPagaron():
        return CobroTarifa.__totalClientesPagaron
        
    def renew():
        CobroTarifa.__totalGastoAC = 0
        CobroTarifa.__totalClientesPagaron = 0

    #instance
    def __init__(self, servidor: Servidor, cola: Cola, colaSigEvento: Cola) -> None:
        super().__init__(servidor, cola, colaSigEvento)
        self.__req_accion_especifica = True
    
    def ocurrir(self) -> None:
        super().ocurrir()
        if self._cliente.imprimioAlgo():
            self._colaSigEvento.agregar(self._cliente)
            self._cliente.esperar_retiro_impresiones()
        else:
            self._cliente.irse()
        
        CobroTarifa.__totalClientesPagaron += 1
        CobroTarifa.__totalGastoAC += self._cliente.getCostoTotal()
    
    def _calcularTardanza(self) -> float:
        # Metodo Hook para actualizarEstado(), se recuperan las decisiones del cliente
        return 0.5 # siempre se tarda 30 segs