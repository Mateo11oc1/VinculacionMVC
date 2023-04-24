import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.uic.properties import QtWidgets

from controlador.CtrlReporteErrores import *
from vista.reportes import Ventana

if __name__ == '__main__':
    app = QApplication(sys.argv)
    c=Ventana()
    sys.exit(app.exec())