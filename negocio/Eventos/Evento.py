
from typing import List
from ..Cliente import Cliente
from ..Cola import Cola
from ..Servidores.Servidor import Servidor

class Evento:
    #static
    __lista_eventos: List = []

    def renew():
        Evento.__lista_eventos = []
        
    def getListaEventos():
        return Evento.__lista_eventos

    def __init__(self, servidor:Servidor, cola:Cola, colaSigEvento:Cola) -> None:
        self._servidor: Servidor = servidor
        self._cliente: Cliente | None = None
        self._cola: Cola = cola
        self._colaSigEvento: Cola | None = colaSigEvento
        self._horaSigOcurrencia: float = 0
        self._tardanza: float = 0
        self._activo: bool = False # indica si el evento esta en proceso

        # se autoagrega a la lista 
        Evento.__lista_eventos.append(self)

    def ocurrir(self) -> None:
        '''Marca el fin de espera de un evento, su nuevo estado se visualiza al actualizar'''
        # en este metodo de debe solucionar lo siguiente:
        # 1 si el cliente que genero el evento se dirige a otro evento o se va del sistema
        # 2 cambiar el estado del cliente saliente

        if not self._colaSigEvento is None:
            self._colaSigEvento.agregar(self._cliente)
        self._servidor.liberar()

        # el evento pasa a estar inactivo
        self._activo = False


    def actualizarEstado(self, relojSistema: float) -> None:
        '''Accion necesaria en cada iteracion, descubre nuevos clientes y estados'''

        if not self._cola.estaVacia():

            # cliente y servidor
            self._cliente = self._cola.siguiente()
            self._ocuparCliente(self._cliente)
            self._servidor.ocupar()

            # evento
            self._activo = True
            
            # ultimos calculos
            self._tardanza = self._calcularTardanza()
            self._horaSigOcurrencia = relojSistema +  self._tardanza


    def _ocuparCliente(self, cliente: Cliente):
        # Metodo Hook para actualizarEstado(), avisa al cliente que es su turno para el evento
        pass

    def _calcularTardanza(self) -> float:
        # Metodo Hook para actualizarEstado(), se recuperan las decisiones del cliente
        pass
    
    def getHoraSigOcurrencia(self) -> float:
        return self._horaSigOcurrencia

    def getCola(self):
        return self._cola

    def getServidor(self):
        return self._servidor

    def estaActivo(self):
        return self._activo