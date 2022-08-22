from .Servidor import Servidor
from enum import Enum


class _Estados(Enum):
    OCUPADO = "Ocupada"
    LIBRE = "Libre"

class Impresora(Servidor):
    def __init__(self) -> None:
        super().__init__()
        self.__nombre = "Impresora"
        self.__estados = _Estados
        self.__estado = self.__estados.LIBRE