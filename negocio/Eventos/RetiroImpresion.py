from .Evento import Evento
from ..Cliente import Cliente
from ..Cola import Cola
from ..Servidores.Servidor import Servidor

class RetiroImpresion(Evento):
    def __init__(self, servidor: Servidor, cola: Cola, colaSigEvento: Cola) -> None:
        super().__init__(servidor, cola, colaSigEvento)

    def ocurrir(self) -> None:
        self._cliente.irse()
    
    def _calcularTardanza(self) -> float:
        # Metodo Hook para actualizarEstado(), se recuperan las decisiones del cliente
        return 1 # siempre tarda 1 min