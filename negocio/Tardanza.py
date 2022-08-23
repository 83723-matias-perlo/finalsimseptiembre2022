from random import Random

class Tardanza:

    def __init__(self, generador: Random, dias_media=3) -> None:
        self.__generador_rnd = generador
        self.__dias_media = dias_media

    def getTardanza(self):
        return self.__generador_rnd.expovariate(1 / self.__dias_media)