
from pathlib import Path
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem
# from PyQt5.QtCore import QObject, QThread, pyqtSignal

from negocio.Simulador import SimuladorMontecarloSimple, VectorEstado
from interfaces.ui_params import UiParams
from interfaces.Ui_Ejercicio import UiEjercicio
from soporte.Parametros import Parametros

class UiMain(QtWidgets.QMainWindow):
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        self.loadUi()
        # self.parametros: Parametros = None
        self.vtnParams: UiParams = UiParams()
        self.vtnEjercicio: UiEjercicio = UiEjercicio()
    
    def setParametros(self, params: Parametros):
        self.parametros = params

    def loadUi(self):
        # carga ui
        qtcreator_file = Path(__file__).resolve().parent / "qt" / "main_v2.ui"
        uic.loadUi(qtcreator_file, self)

        # configuracion
        self.configurarTabla()

        # bindings
        self.actionGenerar_Simulacion.triggered.connect(self.cargarSimulaciones)
        self.actionConfigurar_Parametros.triggered.connect(self.cargarVentanaParametros)
        self.actionLimpiarContenido.triggered.connect(self.limpiarContent)
        self.actionSobre_El_Ejercicio.triggered.connect(self.cargarVentanaEjercicio)

    def configurarTabla(self):
        # span
        # climas de los dias
        self.tablaHeader.setSpan(0, 1, 1, 11)
        
        # total de dias por clima
        self.tablaHeader.setSpan(0, 12, 1, 3)

        # tardanza del fertilizante
        self.tablaHeader.setSpan(0, 15, 1, 2)

    def cargarSimulaciones(self):
        self.limpiarContent()
        simulador = SimuladorMontecarloSimple(self.vtnParams.getParams())
        vector: VectorEstado = None
        produccion_ac = 0
        
        for i in range(self.vtnParams.getParams().cant_anios):
            vector = simulador.ejecutarSimulacion()
            self.tablaResultados.insertRow(self.tablaResultados.rowCount())
            self.tablaResultados.setItem(self.tablaResultados.rowCount() - 1, 0, QTableWidgetItem(str(vector.getYear())))
            self.tablaResultados.setItem(self.tablaResultados.rowCount() - 1, 1, QTableWidgetItem(str(self.__truncarFloat(vector.getRndClima(), 4))))
            for i in range(0, 20, 2):
                self.tablaResultados.setItem(self.tablaResultados.rowCount() - 1, 2 + i, QTableWidgetItem(str(vector.getClimaDia(i + 1))))
                self.tablaResultados.setItem(self.tablaResultados.rowCOunt() - 1, 3 + i,  )
            self.tablaResultados.setItem(self.tablaResultados.rowCount() - 1, 12, QTableWidgetItem(str(vector.getCantDiasSoleados())))
            self.tablaResultados.setItem(self.tablaResultados.rowCount() - 1, 13, QTableWidgetItem(str(vector.getCantDiasLluviosos())))
            self.tablaResultados.setItem(self.tablaResultados.rowCount() - 1, 14, QTableWidgetItem(str(vector.getCantDiasNublados())))
            self.tablaResultados.setItem(self.tablaResultados.rowCount() - 1, 15, QTableWidgetItem(str(self.__truncarFloat(vector.getRndTardanzas(), 4))))
            self.tablaResultados.setItem(self.tablaResultados.rowCount() - 1, 16, QTableWidgetItem(str(vector.getDiasTardanza())))
            self.tablaResultados.setItem(self.tablaResultados.rowCount() - 1, 17, QTableWidgetItem(str(self.__truncarFloat(vector.getProduccionTotalAnual(), 4))))
            produccion_ac += vector.getProduccionTotalAnual()
            self.tablaResultados.setItem(self.tablaResultados.rowCount() - 1, 18, QTableWidgetItem(str(self.__truncarFloat(produccion_ac, 4))))
    
    def cargarVentanaParametros(self):
        self.vtnParams.show()
    
    def cargarVentanaEjercicio(self):
        self.vtnEjercicio.show()
        
    def limpiarContent(self):
        self.tablaResultados.setRowCount(0)

    def __truncarFloat(self, num:float, decimales:int) -> float:
        numero = str(num).split(".")
        return float(numero[0] + "." + numero[1][:decimales])





        




