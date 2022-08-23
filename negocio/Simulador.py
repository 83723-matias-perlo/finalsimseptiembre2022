from random import Random

from negocio.Tardanza import Tardanza
from .Dia import Dia, Clima

class SimuladorMontecarloSimple:
    def __init__(self) -> None:

        # generadores de numeros pseudoaleatorios
        self.__generador_clima = None
        self.__generador_tardanza = None # recordar para obtener exponencial se usa la funcion expovariate()

        # datos del vector estado
        self.__year = 0
        self.__rnd_clima = 0
        self.__dias: list[Dia] = []
        self.__contadores_dias = {
            Clima.SOLEADO.value: 0,
            Clima.LLUVIA.value: 0,
            Clima.NUBLADO.value: 0
        }
        self.__rnd_tardanzas = 0
        self.__dias_tardanza = 0
        self.__produccion_anual = 0


    def iniciar(self) -> None:
        self.__generador_clima = Random(5)
        self.__generador_tardanza = Random(14)

        Dia.setGeneradorClima(self.__generador_clima)
        for i in range(10):
            self.__dias += Dia()
            self.__contadores_dias[self.__dias[i].getClima()] += 1

        self.__rnd_tardanzas = Tardanza(self.__generador_tardanza, 3)
        self.__dias_tardanza = self.__rnd_tardanzas.getTardanza()

        self.__produccion_anual = 3350 + 250 * (self.__contadores_dias[Clima.SOLEADO.value] / 10) + 390 * (self.__contadores_dias[Clima.LLUVIA.value] / 10) - 150 * (self.__contadores_dias[Clima.NUBLADO.value] / 10) -600 * self.__dias_tardanza
        

    def siguiente(self) -> None:
        self.__year += 1
        self.__rnd_clima = Dia.getRndInicial()
        
    def reiniciar(self):
        self.__year = 0
        self.__rnd_clima = 0
        self.__dias = [None * 10]
        # self.__dias_soleados = 0
        # self.__dias_lluviosos = 0
        # self.__dias_nublados = 0
        self.__rnd_tardanzas = 0
        self.__dias_tardanza = 0
        self.__produccion_anual = 0

        self.iniciar()
    

    # gets de los valores importantes de la simulacion
    def getYear(self) -> int:
        return self.__year

    def getRndClima(self) -> float:
        return self.__rnd_clima

    def getClimaDia(self, dia: int) -> str:
        return self.__dias[dia - 1].getClima()

    def getCantDiasSoleados(self) -> int:
        return self.__dias_soleados

    def getCantDiasLluviosos(self) -> int:
        return self.__dias_lluviosos

    def getCantDiasNublados(self) -> int:
        return self.__dias_nublados

    def getRndTardanzas(self) -> float:
        return self.__rnd_tardanzas

    def getDiasTardanza(self) -> int:
        return self.__dias_tardanza

    def getProduccionTotalAnual(self) -> float:
        return self.__produccion_anual