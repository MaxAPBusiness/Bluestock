# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'movimientos.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(910, 600)
        MainWindow.setStyleSheet(u"@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@200;400;700&display=swap');\n"
"\n"
"*{\n"
"    font-family: 'Raleway-blod';\n"
"    font-weight: 400;\n"
"}\n"
"\n"
"QMenuBar{\n"
"\n"
"    background-color: #293045;\n"
"    padding: 0;    \n"
"    text-transform: capitalize;\n"
"    font-size: 14px;\n"
"    color:white;\n"
"    display: flex;\n"
"    flex-direction: column;\n"
"\n"
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
"    borde"
                        "r-style: solid;\n"
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
"    font-size: 20px;\n"
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
"    border-radius: 5px;\n"
"    background-color: #BABFCE;\n"
"    color:#293045;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:#768AC5;\n"
"    color:aliceblue;\n"
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
"#pushButton_2,#pushButton_3,#pushButton_4{\n"
"    width: 65px;\n"
"    height: 30px;\n"
""
                        "}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(0, 70))
        font = QFont()
        font.setFamilies([u"Raleway-blod"])
        font.setBold(False)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setPixmap(QPixmap(u"lupa.png"))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setMinimumSize(QSize(340, 0))
        font1 = QFont()
        font1.setFamilies([u"Raleway-blod"])
        font1.setPointSize(11)
        font1.setBold(False)
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 20, -1, 20)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_3.addWidget(self.comboBox)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(35, 16777215))

        self.horizontalLayout_3.addWidget(self.label_4)

        self.dateTimeEdit = QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")

        self.horizontalLayout_3.addWidget(self.dateTimeEdit)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(32, 16777215))

        self.horizontalLayout_3.addWidget(self.label_5)

        self.dateTimeEdit_2 = QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit_2.setObjectName(u"dateTimeEdit_2")

        self.horizontalLayout_3.addWidget(self.dateTimeEdit_2)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_3.addWidget(self.comboBox_2)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 0))
        self.label_7.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_3.addWidget(self.label_7)

        self.comboBox_3 = QComboBox(self.centralwidget)
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout_3.addWidget(self.comboBox_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(0, 4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(0, 5, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(0, 6, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(0, 7, __qtablewidgetitem16)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy2)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QFrame.Plain)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(110)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.tableWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(60, -1, 60, -1)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        font2 = QFont()
        font2.setFamilies([u"Raleway-blod"])
        font2.setPointSize(12)
        font2.setBold(False)
        self.pushButton_2.setFont(font2)
        self.pushButton_2.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Gesti\u00f3n de movimiento de herramientas", None))
        self.label_2.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar...", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Persona:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Todos", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Desde:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Hasta:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Herramienta:", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Todas", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Estado:", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Cualquiera", None))

        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Herramienta", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Estado", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Nombre y Apellido", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Clase", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Tipo", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Turno de pa\u00f1olero", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem8 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Martillo", None));
        ___qtablewidgetitem9 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Roto", None));
        ___qtablewidgetitem10 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Juan Minujin", None));
        ___qtablewidgetitem11 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"7 C", None));
        ___qtablewidgetitem12 = self.tableWidget.item(0, 4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"18/02/1819", None));
        ___qtablewidgetitem13 = self.tableWidget.item(0, 5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem14 = self.tableWidget.item(0, 6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Martillo de martillos", None));
        ___qtablewidgetitem15 = self.tableWidget.item(0, 7)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Ayer", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
    # retranslateUi

