from random import Random


class Dia:
    __rnd_inicial = -1
    __dia_inicial: bool = True
    __generador_clima: Random = None
    
    def __init__(self, generador: Random) -> None:
        self.__clima: str = ''
    
    def calcularClima(self) -> str:
        rnd = Dia.getRndInicial() if Dia.__dia_inicial else Dia.__generador_clima.uniform(0,1)
        # TODO: Recuperar tabla de climas, calcular a que clima corresponde

    def getClima(self) -> str:
        return self.__clima

    def getRndInicial():
        if Dia.__rnd_inicial == -1:
            Dia.__rnd_inicial = Dia.__generador_clima.uniform(0,1)
        return Dia.__rnd_inicial