from .Evento import Evento
from ..Cliente import Cliente
from ..Cola import Cola
from ..Servidores.Servidor import Servidor

class PedidoBar(Evento):
    def __init__(self, servidor: Servidor, cola: Cola, colaSigEvento: Cola) -> None:
        super().__init__(servidor, cola, colaSigEvento)

    def ocurrir(self) -> None:
        super().ocurrir()
        self._cliente.navegar()

    def _ocuparCliente(self, cliente: Cliente):
        # Metodo Hook para actualizarEstado(), avisa al cliente que es su turno para el evento
        cliente.esperar_pedido()

    def _calcularTardanza(self) -> float:
        # Metodo Hook para actualizarEstado(), se recuperan las decisiones del cliente
        return 3 # Siempre tarda 3 mins