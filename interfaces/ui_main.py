
from pathlib import Path
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QObject, QThread, pyqtSignal

# from Params import PSim


# qtcreator_file = Path(__file__).resolve().parent / "qt" / "main.ui"
# Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file) #Archivo XML del QtDesigner (extension .ui)

# class UiMain(QtWidgets.QMainWindow, Ui_MainWindow):
class UiMain(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        self.loadUi()
    
    def loadUi(self):
        # carga ui
        qtcreator_file = Path(__file__).resolve().parent / "qt" / "main.ui"
        uic.loadUi(qtcreator_file, self)

        # configuracion
        self.configurarTabla()

        # bindings
        

    def configurarTabla(self):
        # span
        # climas de los dias
        self.tablaResultados.setSpan(0, 1, 1, 11)
        
        # total de dias por clima
        self.tablaResultados.setSpan(0, 12, 1, 3)

        # tardanza del fertilizante
        self.tablaResultados.setSpan(0, 15, 1, 2)