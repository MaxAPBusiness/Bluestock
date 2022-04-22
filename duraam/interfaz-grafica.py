import sys
import PyQt6.QtWidgets as qtw
import PyQt6.QtCore as qtc

class MainWindow(qtw.QMainWindow):
   #hacemos el init
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Jorgito")

        self.label=qtw.QLabel("Introduzca su correo: ")
        self.entry=qtw.QLineEdit()

        self.label2=qtw.QLabel("Introduzca su contraseña: ")
        self.entry2=qtw.QLineEdit()
        self.entry2.setEchoMode(qtw.QLineEdit.EchoMode.Password)
        layout = qtw.QGridLayout()


        layout.addWidget(self.label, 0,0)
        layout.addWidget(self.entry, 0,1)

        layout.addWidget(self.label2, 1,0)
        layout.addWidget(self.entry2, 1,1)

        widget = qtw.QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget) 

app = qtw.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()