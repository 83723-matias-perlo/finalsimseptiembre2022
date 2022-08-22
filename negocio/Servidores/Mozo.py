from .Servidor import Servidor
from enum import Enum


class _Estados(Enum):
    OCUPADO = "Atendiendo"
    LIBRE = "Libre"
    
class Mozo(Servidor):
    def __init__(self) -> None:
        super().__init__()
        self.__nombre = "Mozo"
        self.__estados = _Estados
        self.__estado = self.__estados.LIBRE