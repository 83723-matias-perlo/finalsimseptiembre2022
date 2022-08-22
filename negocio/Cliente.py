from enum import Enum
from random import Random
from typing import List

class _Estados(Enum):
    ESPERANDO_TURNO = "Esperando Turno"
    TOMANDO_TURNO = "Tomando Turno"
    ESPERANDO_MOZO = "Esperando Mozo"
    ESPERANDO_PEDIDO = "Esperando Pedido"
    NAVEGANDO = "Navegando"
    ESPERANDO_COBRO = "Esperando Cobro"
    PAGANDO_TARIFA = "Pagando Tarifa"
    ESPERANDO_RETIRO_IMPRESIONES = "Esperando Retirar Impresiones"
    RETIRANDO_IMPRESIONES = "Retirando Impresiones"
    FINAL = "-"


class Cliente:

    # static
    __id_counter = 0

    # valores para los randoms generados
    __rnd_tipo_turno: Random | None = None
    __rnd_ordenar_bar: Random | None = None
    __rnd_costo_pedido: Random | None = None    # para exponencial es --> random.expovariate(lambda)
    __rnd_hacer_impresiones: Random | None= None
    __lamda_costo_pedido: float = 0

    # lista de clientes generados
    __clientes_lista: List = []

    def __getId():
        nuevo_id = Cliente.__id_counter
        Cliente.__id_counter += 1
        return nuevo_id 

    def __getRNDTurno(seed: float = 1):
        if Cliente.__rnd_tipo_turno is None:
            Cliente.__rnd_tipo_turno = Random(seed)
        return Cliente.__rnd_tipo_turno

    def __getRNDPedidoBar(seed: float = 1):
        if Cliente.__rnd_ordenar_bar is None:
            Cliente.__rnd_ordenar_bar = Random(seed)
        return Cliente.__rnd_ordenar_bar

    def __getRNDCostoPedido(seed:float, lmbda: float):
        '''El RND es exponencial porque se usa con promedio, usa expovariate'''
        if Cliente.__rnd_costo_pedido is None:
            Cliente.__rnd_costo_pedido = Random(seed)
            Cliente.__lamda_costo_pedido = lmbda
        return Cliente.__rnd_costo_pedido

    def __getRNDImpresiones(seed: float = 1):
        if Cliente.__rnd_hacer_impresiones is None:
            Cliente.__rnd_hacer_impresiones = Random(seed)
        return Cliente.__rnd_hacer_impresiones

    def getListaClientes() -> List:
        '''Lista de clientes creados'''
        return Cliente.__clientes_lista
    
    def setParams(
        seedTurno: float,
        seedPedido: float,
        seedCostoPedido: float,
        promCostoPedido: float,
        seedImpresiones: float) -> None:
        '''Toma las semillas y datos para configurar los generadores'''
        Cliente.__rnd_tipo_turno =  Cliente.__getRNDTurno(seedTurno)
        Cliente.__rnd_ordenar_bar = Cliente.__getRNDPedidoBar(seedPedido)
        Cliente.__rnd_costo_pedido = Cliente.__getRNDCostoPedido(seedCostoPedido, 1 / promCostoPedido)
        Cliente.__rnd_hacer_impresiones = Cliente.__getRNDImpresiones(seedImpresiones)
        

    def renew():
        '''Reinicia los valores estaticos para comenzar una nueva simulacion'''
        Cliente.__id_counter = 0
        Cliente.__rnd_tipo_turno = None
        Cliente.__rnd_ordenar_bar = None
        Cliente.__rnd_costo_pedido = None
        Cliente.__rnd_hacer_impresiones = None
        Cliente.__clientes_lista = []
        Cliente.__lamda_costo_pedido = 0


    # instance
    def __init__(self) -> None:
        self.__id = Cliente.__getId()

        # los generadores de numeros y variables para la toma de decision
        self.__rnd_tipo_turno = Cliente.__rnd_tipo_turno
        self.__rnd_ordenar_bar = Cliente.__rnd_ordenar_bar
        self.__rnd_costo_pedido = Cliente.__rnd_costo_pedido
        self.__rnd_impresiones = Cliente.__rnd_hacer_impresiones

        # rnds de decision
        self.__rnd_decision_turno: float = 0
        self.__rnd_decision_pedir: float = 0
        self.__rnd_decision_costo_pedido: float = 0
        self.__rnd_decision_imprime: float = 0

        # gestores del estado del cliente
        self.__estados = _Estados
        self.__estado = self.__estados.ESPERANDO_TURNO
        self.__costo_total: float = 0

        # valores de las decisiones tomadas por este cliente particular
        self.__turno: int = 0
        self.__pide_del_bar: bool | None = None
        # self.__costo_de_pedido: float = 0
        self.__imprime_algo: bool | None = None

        # se autoagrega a la lista 
        Cliente.__clientes_lista.append(self)

    def __str__(self) -> str:
        return f"Cliente - {self.__id}"
        
    # getters de los valores de decision de este cliente 

    def getTurno(self) -> int:
        '''Retorna la cantidad de minutos que pidio de turno (30 mins o 60 mins), como entero'''
        return self.__turno

    def imprimioAlgo(self) -> bool:
        return self.__imprime_algo

    def ordenaAlgoDelBar(self) -> bool:
        self.__pide_del_bar

    # def getCostoPedido(self) -> float:
    #     return self.__costo_de_pedido

    def getCostoTotal(self) -> float:
        return self.__costo_total


    # getters de los rnds de decision de este cliente
    def getRndDecisionTurno(self) -> float:
        return self.__rnd_decision_turno

    def getRndDecisionPedirBar(self) -> float:
        return self.__rnd_decision_pedir

    def getRndDecisionCostoPedido(self) -> float:
        return self.__rnd_decision_costo_pedido
    
    def getRndDecisionImprime(self) -> float:
        return self.__rnd_decision_imprime


    # Metodos de cambio de estado y calculo de decisiones
    def tomar_turno(self):
        if self.__estado == self.__estados.ESPERANDO_TURNO:
            self.__estado = self.__estados.TOMANDO_TURNO

            self.__rnd_decision_turno = self.__rnd_tipo_turno.random()
            if self.__rnd_decision_turno < 0.5:
                self.__turno = 60
                self.__costo_total += 3.50
            else:
                self.__turno = 30
                self.__costo_total += 2

    def getEstado(self) -> str:
        return self.__estado.value

    def navegar(self):
        if self.__estado in [self.__estados.TOMANDO_TURNO, self.__estados.ESPERANDO_PEDIDO]:
            self.__estado = self.__estados.NAVEGANDO

            # decision de pedir en el bar
            self.__rnd_decision_pedir = self.__rnd_ordenar_bar.random()
            self.__pide_del_bar = True if self.__rnd_decision_pedir < 0.2 else False

    def esperar_mozo(self):
        if self.__estado == self.__estados.NAVEGANDO:
            self.__estado = self.__estados.ESPERANDO_MOZO

    def esperar_pedido(self):
        if self.__estado == self.__estados.ESPERANDO_MOZO:
            self.__estado = self.__estados.ESPERANDO_PEDIDO
            self.__rnd_decision_costo_pedido = self.__rnd_costo_pedido.expovariate(Cliente.__lamda_costo_pedido)
            self.__costo_total += self.__rnd_decision_costo_pedido

    def esperar_cobro(self):
        if self.__estado == self.__estados.NAVEGANDO:
            self.__estado = self.__estados.ESPERANDO_COBRO
            
            self.__rnd_decision_imprime = self.__rnd_impresiones.random()
            if self.__rnd_decision_imprime < 0.1:
                self.__imprime_algo = True
                self.__costo_total += 0.5
            else:
                self.__imprime_algo = False

    def pagar_tarifa(self):
        if self.__estado == self.__estados.ESPERANDO_COBRO:
            self.__estado = self.__estados.PAGANDO_TARIFA

    def esperar_retiro_impresiones(self):
        if self.__estado == self.__estados.PAGANDO_TARIFA:
            self.__estado = self.__estados.ESPERANDO_RETIRO_IMPRESIONES

    def retirar_impresiones(self):
        if self.__estado == self.__estados.ESPERANDO_RETIRO_IMPRESIONES:
            self.__estado = self.__estados.RETIRANDO_IMPRESIONES
    
    def irse(self):
        if self.__estado in [self.__estados.PAGANDO_TARIFA, self.__estados.RETIRANDO_IMPRESIONES]:
            self.__estado = self.__estados.FINAL
