
from .Servidor import Servidor
from enum import Enum


class _Estados(Enum):
    OCUPADO = "Ocupada"
    LIBRE = "Libre"

class Terminal(Servidor):
    # static
    __id_counter = 0

    def __getId():
        nuevo_id = Terminal.__id_counter
        Terminal.__id_counter += 1
        return nuevo_id

    def renew():
        Terminal.__id_counter = 0 

    # instance
    def __init__(self) -> None:
        super().__init__()
        self.__id = Terminal.__getId()
        self.__nombre = "Terminal"
        self.__estados: Enum = _Estados
        self.__estado: str = self.__estados.LIBRE
        
    def __str__(self):
        return f"{self.__nombre} - {self.__id}"
    
    def estaLibre(self) -> bool:
        return self.__estado == self.__estados.LIBRE