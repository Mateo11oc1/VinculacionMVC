# Form implementation generated from reading ui file 'reportes-errores.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QMovie
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QProgressBar


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        
        MainWindow.resize(1300, 820)
        MainWindow.setStyleSheet(".QPushButton{\n"
"    color: rgb(0, 0, 127);\n"
"    background-color: rgb(255,255,255);\n"
"    border-radius:15;\n"
"\n"
"}\n"
".QPushButton:hover{\n"
"    background-color:#c4c4c4;\n"
"    color:black;\n"
"}\n"
"\n"
"[name = fondoErrores]{\n"
"    background-image: url(\"C:\\Users\\aimbe\\Downloads\\Recurso 6-100\\\")\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1310, 820))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.fondoErrores = QtWidgets.QFrame(self.tab_2)
        self.fondoErrores.setGeometry(QtCore.QRect(0, 0, 1311, 791))
        self.fondoErrores.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.fondoErrores.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.fondoErrores.setObjectName("fondoErrores")
        self.label = QtWidgets.QLabel(self.fondoErrores)
        self.label.setGeometry(QtCore.QRect(0, 0, 1310, 820))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./imagenes/Recurso 6-100.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.fondoErrores)
        self.label_2.setGeometry(QtCore.QRect(50, 30, 631, 291))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("./imagenes/carro.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.fondoErrores)
        self.label_3.setGeometry(QtCore.QRect(1040, 450, 451, 311))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("./imagenes/moto.png"))
        self.label_3.setObjectName("label_3")
         
        self.tblTablaErrores = QtWidgets.QTableView(self.fondoErrores)
        self.tblTablaErrores.setGeometry(QtCore.QRect(30, 270, 1222, 440))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tblTablaErrores.setStyleSheet("background-color: rgb(255,255,255);\n"
"border-radius:15;\n"
"\n"
"")
        self.tblTablaErrores.setObjectName("tblTablaErrores")
        self.btnVerObservaciones = QtWidgets.QPushButton(self.fondoErrores)
        self.btnVerObservaciones.setGeometry(QtCore.QRect(140, 150, 211, 61))
        self.btnVerObservaciones.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./imagenes/ver-observaciones.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnVerObservaciones.setIcon(icon)
        self.btnVerObservaciones.setIconSize(QtCore.QSize(50, 50))
        self.btnVerObservaciones.setObjectName("btnVerObservaciones")
        self.btnSeleccionarArchivo = QtWidgets.QPushButton(self.fondoErrores)
        self.btnSeleccionarArchivo.setGeometry(QtCore.QRect(520, 150, 211, 61))
        self.btnSeleccionarArchivo.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./imagenes/archivos.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnSeleccionarArchivo.setIcon(icon1)
        self.btnSeleccionarArchivo.setIconSize(QtCore.QSize(50, 50))
        self.btnSeleccionarArchivo.setObjectName("btnSeleccionarArchivo")
        self.btnSeleccionarCarpeta = QtWidgets.QPushButton(self.fondoErrores)
        self.btnSeleccionarCarpeta.setGeometry(QtCore.QRect(850, 150, 211, 61))
        self.btnSeleccionarCarpeta.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./imagenes/seleccionar-carpteta.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnSeleccionarCarpeta.setIcon(icon2)
        self.btnSeleccionarCarpeta.setIconSize(QtCore.QSize(50, 50))
        self.btnSeleccionarCarpeta.setObjectName("btnSeleccionarCarpeta")
        self.label_4 = QtWidgets.QLabel(self.fondoErrores)
        self.label_4.setGeometry(QtCore.QRect(390, 60, 471, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
         
        self.label_6 = QtWidgets.QLabel(self.fondoErrores)
        self.label_6.setGeometry(QtCore.QRect(670, 780, 231, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.fondoErrores)
        self.label_7.setGeometry(QtCore.QRect(620, 780, 231, 21))
        self.label_7.setObjectName("label_7")
        self.label.raise_()
         
        self.label_3.raise_()
        self.btnSeleccionarCarpeta.raise_()
        self.label_2.raise_()
        self.btnVerObservaciones.raise_()
        self.label_4.raise_()
        self.tblTablaErrores.raise_()
        self.btnSeleccionarArchivo.raise_()
         
        self.label_6.raise_()
        self.label_7.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.btnVerObservaciones.setToolTip(_translate("MainWindow", "Seleccione una carpeta para ver las observaciones que tienen los tramos de manera resumida en la tabla "))
        self.btnVerObservaciones.setText(_translate("MainWindow", "Ver observaciones"))
        self.btnSeleccionarArchivo.setToolTip(_translate("MainWindow", "Seleccione un solo archivo excel que desee validar, en la tabla se presentará un resumen de los errores"))
        self.btnSeleccionarArchivo.setText(_translate("MainWindow", "Seleccionar archivo"))
        self.btnSeleccionarCarpeta.setToolTip(_translate("MainWindow", "Seleccione una carpeta que contenga archivos excel para validarlos"))
        self.btnSeleccionarCarpeta.setText(_translate("MainWindow", "Seleccionar carpeta"))
        self.label_4.setText(_translate("MainWindow", " REPORTES DE ERRORES"))
        self.label_4.setStyleSheet("color: white; font-size: 30pt; font-weight: bold;")
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Reporte de errores"))
        loading_widget = LoadingWidget()
        #addWidget(loading_widget)


"""if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
"""
class Ventana(QtWidgets.QMainWindow):
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Validacion y verificacion de datos")
        self.setWindowIcon(QIcon("./imagenes/icono-ventana.png"))
        self.show()
       




class LoadingWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Configurar el layout
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Añadir el label con el mensaje de carga
        self.loading_label = QLabel("Cargando...")
        layout.addWidget(self.loading_label)

        # Añadir la animación de carga
        self.loading_movie = QMovie("./imagenes/cargando.gif")
        self.loading_label.setMovie(self.loading_movie)
        self.loading_movie.start()

        # Añadir la barra de progreso
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)

    def set_progress(self, value):
        self.progress_bar.setValue(value)

       
