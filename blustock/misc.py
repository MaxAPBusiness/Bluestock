"""Este módulo contiene funciones miscelánea útiles para el programa.

Funciones
---------
    mostrarContrasena(boton, entry: QtWidgets.QLineEdit):
        Muestra o esconde lo ingresado en el campo de contraseña
        vinculado dependiendo del estado de activación del botón.
"""
import os
import types
from PyQt6 import QtWidgets, QtGui, QtCore
from ui.presets.popup import PopUp
from ui.presets.param_edit import ParamEdit

def mostrarContrasena(boton: QtWidgets.QCheckBox, entry: QtWidgets.QLineEdit):
    """Este método muestra o esconde lo ingresado en el campo de
    contraseña vinculado dependiendo del estado de activación del 
    botón.

    Parámetros
    ----------
        boton: QtWidgets.QCheckBox
            El botón que esconde/muestra la contraseña.
        entry : QtWidgets.QLineEdit
            El entry de contraseña vinculado al botón.
    """
    # Si el botón está presionado
    if boton.isChecked():
        # Muestra lo ingresado en el campo.
        entry.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        # Cambia el ícono.
        path = f'ui{os.sep}rsc{os.sep}icons{os.sep}esconder.png'
        pixmap = QtGui.QPixmap(path)
    else:
        # Cifra lo ingresado en el campo.
        entry.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        path = f'ui{os.sep}rsc{os.sep}icons{os.sep}mostrar.png'
        pixmap = QtGui.QPixmap(path)
    boton.setIcon(QtGui.QIcon(pixmap))
    boton.setIconSize(QtCore.QSize(25, 25))

camposStock=(2, 1, 1, 0, 0, 2, 2, 4, 3, 3)

def insertarFilas(self, tabla: QtWidgets.QTableWidget,
                  funcGuardar: types.FunctionType,
                  funcEliminar: types.FunctionType,
                  campos: tuple, sugerencias: tuple | list | None = None,
                  funcEspecial: types.FunctionType | None = None):
    """Este método inserta una nueva fila en una tabla de una gestión.

    Parámetros
    ----------
        tabla: QtWidgets.QTableWidget
            La tabla a la que se le van a insertar los elementos.
        camposObligatorios: tuple
            Los campos de la fil anterior que se van a verificar
            para que no estén en blanco, evitando así que se puedan
            insertar múltiples filas en blanco.
        funcGuardar: types.FunctionType
            La función guardar que el botón guardar de la fila
            ejecutará.
        funcEliminar: types.FunctionType
            La función eliminar que el botón eliminar de la fila
            ejecutará.
    """
    # Desconectamos la tabla para que no genere problemas
    try:
        tabla.disconnect()
    except:
        pass
    # Obtenemos el índice final, en el cual agregaremos la fila.
    indiceFinal = tabla.rowCount()

    # Antes de agregar la fila, queremos comprobar que la última
    # fila de la tabla no tenga campos vacíos. Esto lo hacemos
    # para que el usuario no pueda ingresar múltiples filas vacías
    # haciendo que el sistema detecte si la fila anterior está
    # vacía.
    ultimaFila = indiceFinal-1
    if ultimaFila >= 0:
        # Por cada campo...
        for nCampo, tipoCampo in enumerate(campos):
            # ... si el campo es obligatorio...
            if tipoCampo in {1, 3, 4}:
                # ...verificamos si el campo es un lineedit o una celda
                # normal, ya que el texto se obtiene de forma
                # diferente, y obtenemos el texto
                if tipoCampo == 1:
                    texto=tabla.item(ultimaFila, nCampo).text()
                else:
                    texto=tabla.cellWidget(ultimaFila, nCampo).text()
                # Si la celda/lineedit está vacía...
                if texto == "":
                    # Le pide al usuario que termine de llenar los
                    # campos y corta la función.
                    mensaje = "Ha agregado una fila y todavía no ha ingresado los datos de la fila anterior. Ingreselos, guardelos cambios e intente nuevamente."
                    return PopUp("Error", mensaje).exec()
                
    # Se añade la fila al final.
    tabla.insertRow(indiceFinal)
    # Movemos la barra hasta el final asi el usuario no tiene que bajar
    # la barra hasta el fondo sino que sea automático.
    tabla.scrollToItem(
        tabla.item(indiceFinal-1, 0),
        QtWidgets.QAbstractItemView.ScrollHint.PositionAtBottom)
    # Añadimos campos de texto en todas las celdas.
    for nCampo, tipoCampo in enumerate(campos):
        if tipoCampo in {0, 1, 2}:
            item=QtWidgets.QTableWidgetItem("")
            if tipoCampo == 2:
                item.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable |
                              QtCore.Qt.ItemFlag.ItemIsEnabled)
            tabla.setItem(indiceFinal, nCampo, item)
        else:
            indice=0
            for i, j in enumerate(campos):
                if j in {3, 4}:
                    if i > nCampo:
                        break
                    else:
                        indice += 1
            campoSugerido = ParamEdit(sugerencias[indice], "")
            if tipoCampo == 4:
                campoSugerido.editingFinished.connect(funcEspecial)
            tabla.setCellWidget(indiceFinal, nCampo, campoSugerido)
        
    generarBotones(funcGuardar, funcEliminar, tabla, indiceFinal)
    tabla.cellWidget(indiceFinal, tabla.columnCount()-2).setEnabled(True)