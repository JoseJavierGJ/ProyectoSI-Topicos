# from PyQt6.QtCore import QPropertyAnimation, QEasingCurve
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QHeaderView, QMessageBox, QPushButton
from PyQt6 import QtWidgets
from PyQt6.uic import loadUi
from conexion_empleado import Comunicacion
from PyQt6.QtCore import QDate

# from PyQt6 import uic 

class EmpleadoWindow(QMainWindow):
  def __init__(self):
    super(EmpleadoWindow, self).__init__()
    loadUi('gui/empleado.ui', self)
    self.llamada = None
    self.Id = None
    
    self.base_datos = Comunicacion()


    # Botones
    self.btnSalir.clicked.connect(self.abrir_login)
    self.btn_refrescar.clicked.connect(self.mostrar_llamadas)
    self.btn_agregar.clicked.connect(self.registrar_llamadas)
    self.btn_borrar.clicked.connect(self.elimina_llamadas)
    # self.btn_actualiza_tabla.clicked.connect(self.modificar_llamadas)
    # self.btn_actualiza_buscar.clicked.connect(self.buscar_por_nombre_actualizar)
    self.btn_buscar_borrar.clicked.connect(self.buscar_por_nombre_eliminar)

    # Conecta las señales a las ranuras
    self.btn_datos.clicked.connect(lambda: self.mostrar_llamadas())
    self.btn_registrar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_registrar))
    # self.btn_actualizar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_actualizar))
    self.btn_eliminar.clicked.connect(lambda: self.mostrar_todos_para_eliminar())  # Modificado aquí
    # self.btn_ajustes.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_ajustes))

    # Conección botones
    self.btn_datos.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_datos))
    self.btn_registrar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_registrar))
    # self.btn_actualizar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_actualizar))
    self.btn_eliminar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_eliminar))
    # self.btn_ajustes.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_ajustes))

    # Ancho de columna adaptable
    self.tabla_borrar.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    self.tabla_llamadas.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

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
      self.tabla_llamadas.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[6]))
      self.tabla_llamadas.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row[7]))
      self.tabla_llamadas.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(row[8]))
      self.tabla_llamadas.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(row[9]))
      tablerow +=1
      # self.signal_actualizar.setText("")
      self.signal_registrar.setText("")
      self.signal_eliminacion.setText("")
  
  
  # En la función registrar_llamadas:
  def registrar_llamadas(self):
    num_empleado = self.reg_nEmpleado.text().upper()
    nombre = self.reg_nombre.text().upper()
    genero = self.reg_genero.currentText().upper()  
    fecha_admision  = self.reg_fecha.date().toPyDate()
    oficio = self.reg_oficio.currentText().upper()  
    telefono = self.reg_telefono.text().upper()
    num_oficina = self.reg_nOficina.text().upper()
    salario = self.reg_salario.text().upper()
    comision = self.reg_comision.text().upper()
    if num_empleado != '' and nombre != '' and genero != '' and fecha_admision != '' and oficio != '' and telefono != '' and num_oficina != '' and salario != '' and comision != '':
        self.base_datos.inserta_llamada(num_empleado, nombre, genero, fecha_admision, oficio, telefono, num_oficina, salario, comision)
        self.signal_registrar.setText('Cliente Registrado')
        self.reg_nEmpleado.clear()
        self.reg_nombre.clear()
        self.reg_genero.setCurrentIndex(0)
        self.reg_oficio.setCurrentIndex(0)
        self.reg_telefono.clear()
        self.reg_nOficina.clear()
        self.reg_salario.clear()
        self.reg_comision.clear()
        self.reg_fecha.setDate(QDate.currentDate())
    else:
        self.signal_registrar.setText('Hay espacios vacios')


    
  def buscar_por_nombre_eliminar(self):
    nombre_llamada = self.eliminar_buscar.text().upper()
    nombre_llamada = str("'" + nombre_llamada + "'")
    llamada = self.base_datos.busca_llamadas(nombre_llamada)
    self.tabla_borrar.setRowCount(len(llamada))

    if len(llamada) == 0:
      self.signal_eliminacion.setText('No existe')
    else:
      self.signal_eliminacion.setText('Llamada seleccionada')
    tablerow = 0
    for row in llamada:
      self.llamada_a_borrar = row[1]
      self.tabla_borrar.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[1]))
      self.tabla_borrar.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[2]))
      self.tabla_borrar.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[3]))
      self.tabla_borrar.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[4]))
      self.tabla_borrar.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[5]))
      self.tabla_borrar.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[6]))
      self.tabla_borrar.setItem(tablerow,6,QtWidgets.QTableWidgetItem(row[7]))
      self.tabla_borrar.setItem(tablerow,7,QtWidgets.QTableWidgetItem(row[8]))
      self.tabla_borrar.setItem(tablerow,8,QtWidgets.QTableWidgetItem(row[9]))
      tablerow +=1

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
          self.signal_eliminacion.setText('Llamada eliminada')
          self.eliminar_buscar.setText('')
      else:
          QMessageBox.warning(self, "Advertencia", "Por favor, seleccione una llamada para eliminar.")

  

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
        self.tabla_borrar.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[6]))
        self.tabla_borrar.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row[7]))
        self.tabla_borrar.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(row[8]))
        self.tabla_borrar.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(row[9]))
        tablerow += 1

if __name__  == '__main__':
    app = QApplication(sys.argv)
    ventana_atencion = EmpleadoWindow()  # Renombrar la instancia
    ventana_atencion.showMaximized()
    sys.exit(app.exec())
