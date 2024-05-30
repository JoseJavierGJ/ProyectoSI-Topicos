import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QHeaderView, QMessageBox
from PyQt6 import QtWidgets
from PyQt6.uic import loadUi
from PyQt6.QtGui import QIntValidator, QRegularExpressionValidator
from PyQt6.QtCore import QDate, QRegularExpression
from conexion_gestion import Comunicacion

class GestionWindow(QMainWindow):
    
    def __init__(self):
        super(GestionWindow, self).__init__()
        loadUi('gui/gestion.ui', self)
        self.llamada = None
        self.Id = None
        
        self.base_datos = Comunicacion()

        # Botones
        self.btnSalir.clicked.connect(self.abrir_login)
        self.btn_refrescar.clicked.connect(self.mostrar_llamadas)
        self.btn_agregar.clicked.connect(self.registrar_llamadas)
        self.btn_borrar.clicked.connect(self.elimina_llamadas)
        self.btn_actualiza_tabla.clicked.connect(self.modificar_llamadas)
        self.btn_actualiza_buscar.clicked.connect(self.buscar_por_nombre_actualizar)
        self.btn_buscar_borrar.clicked.connect(self.buscar_por_nombre_eliminar)

        # Conecta las señales a las ranuras
        self.btn_datos.clicked.connect(lambda: self.mostrar_llamadas())
        self.btn_registrar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_registrar))
        self.btn_actualizar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_actualizar))
        self.btn_eliminar.clicked.connect(lambda: self.mostrar_todos_para_eliminar())
        self.btn_ajustes.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_ajustes))

        # Conexión botones
        self.btn_datos.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_datos))
        self.btn_registrar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_registrar))
        self.btn_actualizar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_actualizar))
        self.btn_eliminar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_eliminar))
        self.btn_ajustes.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_ajustes))

        # Ancho de columna adaptable
        self.tabla_borrar.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tabla_llamadas.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Validaciones
        regex_12_digits = QRegularExpression(r'\d{12}')
        self.reg_tarjeta.setValidator(QRegularExpressionValidator(regex_12_digits, self))
        self.reg_tarjeta.setMaxLength(12)
        self.reg_saldo.setValidator(QRegularExpressionValidator(QRegularExpression(r'\d+(\.\d{1,2})?'), self))
        self.act_buscar.setValidator(QRegularExpressionValidator(regex_12_digits, self))
        self.act_buscar.setMaxLength(12)
        self.eliminar_buscar.setValidator(QRegularExpressionValidator(regex_12_digits, self))
        self.eliminar_buscar.setMaxLength(12)

        # Deshabilitar campos en la sección de actualización
        self.act_tarjeta.setDisabled(True)
        self.act_cliente.setDisabled(True)
        self.act_tipo_tarjeta.setDisabled(True)
        self.act_saldo.setDisabled(True)
        self.act_estado.setDisabled(True)

        # Mostrar datos al abrir la ventana
        self.mostrar_llamadas()     
        
    def abrir_login(self):
        self.close()
        from gui.login import Login
        self.login_window = Login() 
            
    # Configuración página Base de datos
    def mostrar_llamadas(self):
        datos = self.base_datos.mostrar_llamadas()
        i = len(datos)
        self.tabla_llamadas.setRowCount(i)
        tablerow = 0
        for row in datos:
            self.Id = row[0]
            self.tabla_llamadas.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.tabla_llamadas.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[2]))
            self.tabla_llamadas.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[3]))
            self.tabla_llamadas.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[4]))
            self.tabla_llamadas.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[5]))
            tablerow += 1
            self.signal_actualizar.setText("")
            self.signal_registrar.setText("")
            self.signal_eliminacion.setText("")
    
    def registrar_llamadas(self):
        tarjeta = self.reg_tarjeta.text().upper()
        cliente = self.reg_cliente.text().upper()
        tipo_tarjeta = self.reg_tipo_tarjeta.currentText().upper()
        saldo = self.reg_saldo.text()
        estado = self.reg_estado.currentText().upper()  
        if estado == "--- Seleccione una opción":
            QMessageBox.warning(self, "Advertencia", "Debe seleccionar un estado válido.")
            return
        if tarjeta != '' and cliente != '' and tipo_tarjeta != '' and saldo != '' and estado != '':
            self.base_datos.inserta_llamada(tarjeta, cliente, tipo_tarjeta, saldo, estado)
            self.signal_registrar.setText('Tarjeta Registrada')
            self.reg_tarjeta.clear()
            self.reg_cliente.clear()
            self.reg_tipo_tarjeta.setCurrentIndex(0)
            self.reg_saldo.clear()
            self.reg_estado.setCurrentIndex(0)
        else:
            self.signal_registrar.setText('Hay espacios vacíos')

    def buscar_por_nombre_actualizar(self):
        id_llamada = self.act_buscar.text().upper()
        id_llamada = str("'" + id_llamada + "'")
        self.llamada = self.base_datos.busca_llamadas(id_llamada)
        if len(self.llamada) != 0:
            self.Id = self.llamada[0][0]
            self.act_tarjeta.setText(self.llamada[0][1])
            self.act_cliente.setText(self.llamada[0][2])
            self.act_tipo_tarjeta.setText(self.llamada[0][3])
            self.act_saldo.setText(self.llamada[0][4])
            self.act_estado.setText(self.llamada[0][5])
        else:
            self.signal_actualizar.setText("No existe")
        
    def modificar_llamadas(self):
        if self.llamada != '':
            tarjeta = self.act_tarjeta.text().upper()
            cliente = self.act_cliente.text().upper()
            tipo_tarjeta = self.act_tipo_tarjeta.text().upper()
            saldo = self.act_saldo.text()
            estado = self.act_estado_nuevo.currentText().upper()
            if estado == "--- Seleccione una opción":
                QMessageBox.warning(self, "Advertencia", "Debe seleccionar un estado válido.")
                return
            act = self.base_datos.actualiza_llamadas(self.Id, tarjeta, cliente, tipo_tarjeta, saldo, estado)
            if act == 1:
                self.signal_actualizar.setText("Actualizado")
                self.act_tarjeta.clear()
                self.act_cliente.clear()
                self.act_tipo_tarjeta.clear()
                self.act_saldo.clear()
                self.act_estado.clear()
                self.act_estado_nuevo.setCurrentIndex(0)
                self.act_buscar.clear()
            elif act == 0:
                self.signal_actualizar.setText("Error")
            else:
                self.signal_actualizar.setText("Incorrecto")
        else:
            QMessageBox.warning(self, "Advertencia", "No hay tarjeta seleccionada para modificar.")
        
    def buscar_por_nombre_eliminar(self):
        tarjeta = self.eliminar_buscar.text().upper()
        tarjeta = str("'" + tarjeta + "'")
        llamada = self.base_datos.busca_llamadas(tarjeta)
        self.tabla_borrar.setRowCount(len(llamada))

        if len(llamada) == 0:
            self.signal_eliminacion.setText('No existe')
        else:
            self.signal_eliminacion.setText('Tarjeta seleccionada')
        tablerow = 0
        for row in llamada:
            self.llamada_a_borrar = row[1]
            self.tabla_borrar.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.tabla_borrar.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[2]))
            self.tabla_borrar.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[3]))
            self.tabla_borrar.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[4])))
            self.tabla_borrar.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[5]))
            tablerow += 1
    
    def elimina_llamadas(self):
      # Verifica si hay una fila seleccionada en la tabla
        if self.tabla_borrar.currentRow() != -1:
            self.row_flag = self.tabla_borrar.currentRow()
            # Obtiene el nombre de la llamada a eliminar
            self.llamada_a_borrar = self.tabla_borrar.item(self.row_flag, 0).text()
            # Elimina la llamada de la base de datos
            self.base_datos.elimina_llamadas("'" + self.llamada_a_borrar + "'")
            # Elimina la fila de la tabla
            self.tabla_borrar.removeRow(self.row_flag)
            self.signal_eliminacion.setText('Tarjeta eliminada')
            self.eliminar_buscar.setText('')
        else:
            QMessageBox.warning(self, "Advertencia", "Por favor, seleccione una tarjeta para eliminar.")
    
    
    def mostrar_todos_para_eliminar(self):
        datos = self.base_datos.mostrar_llamadas()
        i = len(datos)
        self.tabla_borrar.setRowCount(i)
        tablerow = 0
        for row in datos:
            self.tabla_borrar.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.tabla_borrar.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[2]))
            self.tabla_borrar.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[3]))
            self.tabla_borrar.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[4])))
            self.tabla_borrar.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[5]))
            tablerow += 1

if __name__  == '__main__':
    app = QApplication(sys.argv)
    ventana_gestion = GestionWindow()  # Renombrar la instancia
    ventana_gestion.show()
    sys.exit(app.exec())
