from PyQt6 import QtWidgets, QtCore, QtGui, uic
import sys
import os
os.chdir(f"{os.path.abspath(__file__)}{os.sep}..")
from db.bbdd import BBDD

bbdd=BBDD()
bbdd.refrescarBBDD()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(os.path.abspath(os.getcwd()), f'uis{os.sep}main.ui'), self)

        pantallaAlumnos=QtWidgets.QWidget()
        uic.loadUi(os.path.join(os.path.abspath(os.getcwd()), f'uis{os.sep}alumnos.ui'), pantallaAlumnos)
        pantallaGrupos=QtWidgets.QWidget()
        uic.loadUi(os.path.join(os.path.abspath(os.getcwd()), f'uis{os.sep}grupos.ui'), pantallaGrupos)
        pantallaHerramientas=QtWidgets.QWidget()
        uic.loadUi(os.path.join(os.path.abspath(os.getcwd()), f'uis{os.sep}herramientas.ui'), pantallaHerramientas)
        pantallaHistorial=QtWidgets.QWidget()
        uic.loadUi(os.path.join(os.path.abspath(os.getcwd()), f'uis{os.sep}historial.ui'), pantallaHistorial)
        pantallaMovimientos=QtWidgets.QWidget()
        uic.loadUi(os.path.join(os.path.abspath(os.getcwd()), f'uis{os.sep}movimientos.ui'), pantallaMovimientos)
        pantallaOtroPersonal=QtWidgets.QWidget()
        uic.loadUi(os.path.join(os.path.abspath(os.getcwd()), f'uis{os.sep}otro_personal.ui'), pantallaOtroPersonal)
        pantallaSubgrupos=QtWidgets.QWidget()
        uic.loadUi(os.path.join(os.path.abspath(os.getcwd()), f'uis{os.sep}subgrupos.ui'), pantallaSubgrupos)
        pantallaTurnos=QtWidgets.QWidget()
        uic.loadUi(os.path.join(os.path.abspath(os.getcwd()), f'uis{os.sep}turnos.ui'), pantallaTurnos)
        pantallaUsuarios=QtWidgets.QWidget()
        uic.loadUi(os.path.join(os.path.abspath(os.getcwd()), f'uis{os.sep}usuarios.ui'), pantallaUsuarios)
        pantallas=[pantallaAlumnos, pantallaGrupos, pantallaHerramientas, pantallaHistorial,
                   pantallaMovimientos, pantallaOtroPersonal, pantallaSubgrupos, pantallaTurnos,
                   pantallaUsuarios]
        for pantalla in pantallas:
            self.stackedWidget.addWidget(pantalla)
        
        self.opcionStock.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.opcionSubgrupos.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(6))
        self.opcionGrupos.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.opcionAlumnos.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.opcionOtroPersonal.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(5))
        self.opcionTurnos.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(7))
        self.opcionMovimientos.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.opcionUsuarios.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(8))
        self.opcionHistorial.triggered.connect(lambda: self.stackedWidget.setCurrentIndex(3))

        with open(os.path.join(os.path.abspath(os.getcwd()), 'styles.qss'), 'r') as file:
            self.setStyleSheet(file.read())
        self.stackedWidget.setCurrentIndex(4)
        self.show()

    def login(self):
        bbdd.cur.execute("SELECT count(*) FROM personal WHERE usuario = ?",(self.usuariosLineEdit.text(),))
        check = bbdd.cur.fetchall()
        if check == 1:
            bbdd.cur.execute("SELECT count(*) FROM personal WHERE usuario = ? and contrasena = ?",(self.usuariosLineEdit.text(),self.passwordLineEdit.text(),))
            check = bbdd.cur.fetchall()
            if check == 1:
                self.stackedWidget.setCurrentIndex(1)

app=QtWidgets.QApplication(sys.argv)

for fuente in os.listdir(os.path.join(os.path.abspath(os.getcwd()), f'rsc{os.sep}fonts')):
    QtGui.QFontDatabase.addApplicationFont(
        os.path.join(os.path.abspath(os.getcwd()),
            f'rsc{os.sep}fonts{os.sep}{fuente}')
        )
    
window=MainWindow()
app.exec()
print("God")