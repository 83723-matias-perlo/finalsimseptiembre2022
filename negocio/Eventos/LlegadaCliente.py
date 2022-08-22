from .Evento import Evento
from ..Cliente import Cliente
from ..Cola import Cola
from ..Servidores.Servidor import Servidor

class LlegadaCliente(Evento):
    def __init__(self, servidor: Servidor, cola: Cola, colaSigEvento: Cola) -> None:
        super().__init__(servidor, cola, colaSigEvento)
        self.__reiniciar = True

    def ocurrir(self) -> None:
        '''Evento de tipo Llegada De... , solo crea nuevos clientes y lo pasa al siguiente evento'''

        # cuando ocurre, crea un cliente y lo pasa al siguiente evento
        self._cliente = Cliente()
        if not self._colaSigEvento is None:
            self._colaSigEvento.agregar(self._cliente)
        self.__reiniciar = True


    def actualizarEstado(self, relojSistema: float) -> None:
        '''Accion necesaria en cada iteracion, descubre nuevos clientes y estados'''

        # si recien llega un cliente, se reinicia el proceso de llegada
        if self.__reiniciar:
         
            self._horaSigOcurrencia = relojSistema +  15 # siempre tarda 15 minutos
            self.__reiniciar = False
    
    def getHoraSigOcurrencia(self) -> float:
        return self._horaSigOcurrencia

    def getCola(self):
        return self._cola

    def getServidor(self):
        return self._servidor
    
    def estaActivo(self):
        return True # siempre esta activo
