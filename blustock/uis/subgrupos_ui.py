# Form implementation generated from reading ui file 'c:\Users\mateo\Desktop\Blustock-main\blustock\uis\subgrupos.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(793, 569)
        Form.setStyleSheet("*{\n"
"    font-family: \'Oswald\', sans-serif;\n"
"    font-weight: 400;\n"
"}\n"
"\n"
"QMenuBar{\n"
"    background-color: #293045;\n"
"    padding: 0;    \n"
"    font-size: 14px;\n"
"    color:white;\n"
"}\n"
"\n"
"QMenuBar:item{\n"
"    padding: 17px;\n"
"    border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QMenuBar:item:selected{\n"
"    background-color: #768AC5;\n"
"    color:black;\n"
"    border-radius: 5px;\n"
"    margin: 10px;\n"
"    \n"
"    \n"
"\n"
"}\n"
"\n"
"QMenu{\n"
"    background-color: #293045;\n"
"\n"
"    color: white;\n"
"}\n"
"\n"
"QMenu:item{\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QMenu:item:selected{\n"
"    background-color: #768AC5;\n"
"    color:white;\n"
"\n"
"}\n"
"Qmenu#icon{\n"
"   icon:size 40px; \n"
"    \n"
"}\n"
"\n"
"\n"
"QRadioButton:indicator{\n"
"    border-style: solid;\n"
"    border-color:  #293045;\n"
"    border-radius: 6%;\n"
"    border-width:  2px;\n"
"    background-color: #BABFCE;\n"
"}\n"
"QRadioButton::indicator:checked{\n"
"    background-color: #768AC5;\n"
"}\n"
"\n"
"#label{\n"
"    font-size: 35px;\n"
"}\n"
"\n"
"#usuariosLabel{\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"#contraseALabel{\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"#usuariosLineEdit{\n"
"    width: 170px;\n"
"    height: 20px;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"#passwordLineEdit{\n"
"    width: 170px;\n"
"    height: 20px;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"#labelprofesores{\n"
"    font-size: 26px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    border-radius: 5px;\n"
"    background-color: #BABFCE;\n"
"    \n"
"}\n"
"\n"
"#title{\n"
"    width: 100px;\n"
"    height: 200px;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"    border-color:#293045;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 6px;\n"
"    background-color: #293045;\n"
"    color:#ffffff;\n"
"    padding: 3px 8px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:#768AC5;\n"
"    color:#293045;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #293045;\n"
"\n"
"}\n"
"\n"
"#pushButton_5{\n"
"    padding: 10px;\n"
"    background-color: #768AC5;\n"
"    border-radius: 15%;\n"
"}\n"
"\n"
"")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Oswald")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("c:\\Users\\mateo\\Desktop\\Blustock-main\\blustock\\uis\\lupa.png"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(340, 0))
        font = QtGui.QFont()
        font.setFamily("Oswald")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.checkBox_2 = QtWidgets.QCheckBox(parent=Form)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_2.addWidget(self.checkBox_2)
        self.checkBox = QtWidgets.QCheckBox(parent=Form)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.pushButton_3 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidget = QtWidgets.QTableWidget(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(60, -1, 60, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        font = QtGui.QFont()
        font.setFamily("Oswald")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Gestión de subgrupos"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Buscar..."))
        self.label_3.setText(_translate("Form", "Ordenar:"))
        self.checkBox_2.setText(_translate("Form", "Subgrupo"))
        self.checkBox.setText(_translate("Form", "Grupo"))
        self.pushButton_3.setText(_translate("Form", "^"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Grupo"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Subgrupo"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "-"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "-"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Form", "23"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Form", "002"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("Form", "Editar"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("Form", "Borrar"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("Form", "24"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("Form", "002"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("Form", "Editar"))
        item = self.tableWidget.item(1, 3)
        item.setText(_translate("Form", "Borrar"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_2.setText(_translate("Form", "Agregar"))
