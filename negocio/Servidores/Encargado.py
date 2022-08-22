from ..Cola import Cola
from .Servidor import Servidor
from enum import Enum


class _Estados(Enum):
    OCUPADO = "Asig. Turno"
    LIBRE = "Libre"
    COBRANDO = "Cobr. Tarifa"

class Encargado(Servidor):

    def __init__(self, colaTurnos: Cola, colaCobrar: Cola) -> None:
        super().__init__()
        self.__nombre = "Encargado"
        self.__estados = _Estados
        self.__estado = self.__estados.LIBRE

        self.__cola_para_turnos: Cola = colaTurnos
        self.__cola_para_cobrar: Cola = colaCobrar
        self.__toca_cobrar: bool = False

    def puedeTomarTurnos(self) -> bool:
        return (self.__estado.LIBRE and self.__cola_para_turnos.size() > 0 and
         (not self.__toca_cobrar or self.__cola_para_cobrar.size() == 0))

    def puedeCobrarTarifas(self) -> bool:
        return (self.__estado.LIBRE and self.__cola_para_cobrar.size() > 0 and
         (self.__toca_cobrar or self.__cola_para_turnos.size() == 0))

    def ocupar(self, ParaCobrar=False):
        self.__estado = self.__estados.COBRANDO if ParaCobrar else self.__estados.OCUPADO
        self.__toca_cobrar = False if ParaCobrar else True
