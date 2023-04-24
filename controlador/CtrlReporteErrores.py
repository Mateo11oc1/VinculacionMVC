import sys
import tkinter as tk

from PyQt6.QtWidgets import QWidget
from PyQt6.uic.properties import QtWidgets

from vista.reportes import Ventana


class Principal(QWidget):

    def __init__(self):
        super().__init__()
        self.app=QtWidgets.QApplication(sys.argv)
        self.window=Ventana()
