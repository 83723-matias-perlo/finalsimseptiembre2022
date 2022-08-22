from typing import List

from Negocio.Servidores.Encargado import Encargado
from .Evento import Evento
from ..Servidores.Terminal import Terminal
from ..Cliente import Cliente
from ..Cola import Cola
from ..Servidores.Servidor import Servidor

class AsignacionTerminal(Evento):
    def __init__(self, servidor: Servidor, cola: Cola, colaSigEvento: Cola, colaPedidos: Cola) -> None:
        super().__init__(servidor, cola, colaSigEvento)
        self.__colaPedidos: Cola = colaPedidos
        self.__terminales: List[Terminal] = [] # TODO: Enlazarlos con las terminales
        self.__rnd_decision_turno: float = 0

    def ocurrir(self) -> None:
        super().ocurrir()
        
        if self._cliente.ordenaAlgoDelBar():
            self.__colaPedidos.agregar(self._cliente)
            self._cliente.esperar_mozo()
        else:
            self._cliente.navegar()
    
    def actualizarEstado(self, relojSistema: float) -> None:

        terminal_libre = False
        for terminal in self.__terminales:
            if terminal.estaLibre():
                terminal_libre = True
                break
        
        serv: Encargado = self._servidor
        if serv.puedeTomarTurnos() and terminal_libre:
            super().actualizarEstado()


    def _ocuparCliente(self, cliente: Cliente):
        # Metodo Hook para actualizarEstado(), avisa al cliente que es su turno para el evento
        cliente.tomar_turno()
        self.__rnd_decision_turno = cliente.getRndDecisionTurno()

    def _calcularTardanza(self) -> float:
        # Metodo Hook para actualizarEstado(), se recuperan las decisiones del cliente
        return 20/60 # siempre tarda 20 segs