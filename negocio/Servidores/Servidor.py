from enum import Enum
from typing import List


class _Estados(Enum):
    OCUPADO = "Ocupado"
    LIBRE = "Libre"

class Servidor:

    # static
    __lista_servidores: List = []

    def renew():
        Servidor.__lista_servidores = []

    def getListaServidores():
        return Servidor.__lista_servidores


    # instance
    def __init__(self) -> None:
        
        self.__nombre: str = "Servidor"
        self.__estados: Enum = _Estados
        self.__estado: str = self.__estados.LIBRE

        #se autoagrega a la lista
        Servidor.__lista_servidores.append(self)

    def __str__(self):
        return self.__nombre

    def ocupar(self):
        self.__estado = self.__estados.OCUPADO

    def liberar(self):
        self.__estado = self.__estados.LIBRE

    def getEstado(self):
        return self.__estado.value

if __name__ == "__main__":

    #probando el scope de la asignacion de IDs
    # print(Servidor().getId())
    # print(Servidor().getId())
    # print(Servidor().getId())

    # probando el enumerador de estados
    # print(Servidor().estados.OCUPADO)
    servi = Servidor()
    print(servi.getEstado())

    servi.ocupar()
    print(servi.getEstado())

    servi.liberar()
    print(servi.getEstado())





