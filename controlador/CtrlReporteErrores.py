import sys
import tkinter as tk


from PyQt6.QtWidgets import QWidget, QFileDialog
from PyQt6 import QtWidgets

# from PyQt6.uic.properties import QtWidgets
from vista.reportes import Ventana
from modelo.validaciones import * 

class Controlador(QWidget):

    def __init__(self):
        
        super().__init__()
        # instancio la ventana
        self.app = QtWidgets.QApplication(sys.argv)
        self.vista = Ventana()
        
        #----------------------
        self.modelo = Validaciones()
        
        self.vista.ui.btnSeleccionarCarpeta.clicked.connect(self.buscarCarpeta)
        
        
        
    def buscarCarpeta(self):
        # self.carpeta, ok = QFileDialog.getOpenFileName(self, "Seleccionar carpeta", r"<Default dir>", "Directorios") 
        self.carpeta = QFileDialog.getExistingDirectory(self, "Selecciona una carpeta", "/")
        self.modelo.leerCarpeta(self.carpeta)
        self.modelo.leerColumna()
        
