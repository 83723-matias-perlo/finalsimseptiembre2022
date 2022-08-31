from pathlib import Path

from PyQt5 import QtWidgets
from PyQt5 import QtWidgets, uic


class UiEjercicio(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.loadUi()
    
    def loadUi(self):
        path = Path(__file__).parent.resolve() / "qt" / "ejercicio.ui"
        uic.loadUi(path, self)
    
    