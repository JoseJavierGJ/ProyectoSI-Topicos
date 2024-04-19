# from PyQt6.QtCore import QPropertyAnimation, QEasingCurve
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QHeaderView
from PyQt6 import QtWidgets
from PyQt6.uic import loadUi
from conexion_atencion import Comunicacion
# from PyQt6 import uic 

class AtencionWindow(QMainWindow):
  def __init__(self):
    super(AtencionWindow, self).__init__()
    loadUi('gui/atencion.ui', self)
    # self.main = uic.loadUi("gui/atencion2.ui")
    # self.main.show()
    


    # self.btn_menu.clicked.connect(self.mover_menu)
    self.base_datos = Comunicacion()

    # Ocultar los botones
    # self.btn_restaurar.hide()
    # Botones
    self.btn_refrescar.clicked.connect(self.mostrar_llamadas)
    self.btn_agregar.clicked.connect(self.registrar_llamadas)
    self.btn_borrar.clicked.connect(self.elimina_llamadas)
    self.btn_actualiza_tabla.clicked.connect(self.modificar_llamadas)
    self.btn_actualiza_buscar.clicked.connect(self.buscar_por_nombre_actualizar)
    self.btn_buscar_borrar.clicked.connect(self.buscar_por_nombre_eliminar)

    # Conecta las señales a las ranuras
    self.btn_datos.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_datos))
    self.btn_registrar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_registrar))
    self.btn_actualizar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_actualizar))
    self.btn_eliminar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_eliminar))
    self.btn_ajustes.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_ajustes))

    # SizeGrip
    # self.gripSize = 10
    # self.grip = QtWidgets.QSizeGrip(self)
    # self.grip.resize(self.gripSize, self.gripSize)

    # Mover ventana
    # self.frame_superior.mouseMoveEvent = self.mover_ventana

    # Conección botones
    self.btn_datos.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_datos))
    self.btn_registrar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_registrar))
    self.btn_actualizar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_actualizar))
    self.btn_eliminar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_eliminar))
    self.btn_ajustes.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_ajustes))

    # Ancho de columna adapatable
    self.tabla_borrar.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    self.tabla_llamadas.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

  # Método para mover el menu lateral izquierdo
  # def mover_menu(self):
  #   if True:
  #     width = self.frame_control.width()
  #     normal = 0
  #     if width == 0:
  #       extender = 200
  #     else:
  #       extender = normal
  #     self.animacion = QPropertyAnimation(self.frame_control, b'minimumWidth')
  #     self.animacion.setDuration(300)
  #     self.animacion.setStartValue(width)
  #     self.animacion.setEndValue(extender)
  #     self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
  #     self.animacion.start()
  
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
      tablerow +=1
      self.signal_actualizar.setText("")
      self.signal_registrar.setText("")
      self.signal_eliminacion.setText("")
  
  def registrar_llamadas(self):
    orden = self.reg_orden.text().upper()
    cliente = self.reg_cliente.text().upper()
    motivo = self.reg_motivo.text().upper()
    fecha = self.reg_fecha.text().upper()
    estado = self.reg_estatus.text().upper()
    if orden != '' and cliente != '' and motivo != '' and fecha != '' and estado != '':
      self.base_datos.inserta_llamada(orden, cliente, motivo, fecha, estado)
      self.signal_registrar.setText('Cliente Registrado')
      self.reg_orden.clear()
      self.reg_cliente.clear()
      self.reg_motivo.clear()
      self.reg_fecha.clear()
      self.reg_estatus.clear()
    else:
      self.signal_registrar.settext('Hay espacios vacios')

  def buscar_por_nombre_actualizar(self):
    id_llamada = self.act_buscar.text().upper()
    id_llamada = str("'" + id_llamada + "'")
    self.llamada = self.base_datos.busca_llamadas(id_llamada)
    if len(self.llamada) != 0:
      self.Id = self.llamada[0][0]
      self.act_orden.setText(self.llamada[0][1])
      self.act_cliente.setText(self.llamada[0][2])
      self.act_motivo.setText(self.llamada[0][3])
      self.act_fecha.setText(self.llamada[0][4])
      self.act_estatus.setText(self.llamada[0][5])
    else:
      self.sigmal_actualizar.setText("No existe")
    
  def modificar_llamadas(self):
    if self.llamada != '':
      orden = self.act_orden.text().upper()
      cliente = self.act_cliente.text().upper()
      motivo = self.act_motivo.text().upper()
      fecha = self.act_fecha.text().upper()
      estado = self.act_estatus.text().upper()
      act = self.base_datos.actualiza_llamadas(self.Id, orden, cliente, motivo, fecha, estado)
      if act == 1:
        self.signal_actualizar.setText("Actualizado")
        self.act_orden.clear()
        self.act_cliente.clear()
        self.act_motivo.clear()
        self.act_fecha.clear()
        self.act_estatus.clear()
        self.act_buscar.clear()
      elif act == 0:
        self.signal_actualizar.setText("Error")
      else:
        self.signal_actualizar.setText("Incorrecto")
    
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
      tablerow +=1

  def elimina_llamadas(self):
    self.row_flag = self.tabla_borrar.currentRow()
    if self.row_flag == 0:
      self.tabla_borrar.removeRow(0)
      print("Valor de self.llamada_a_borrar:", self.llamada_a_borrar)
      self.base_datos.elimina_llamadas("'" + self.llamada_a_borrar + "'")
      self.signal_eliminacion.setText('Producto Elminado')
      self.eliminar_buscar.setText('')
      # self.mostrar_llamadas()

if __name__  == '__main__':
    app = QApplication(sys.argv)
    ventana_atencion = AtencionWindow()  # Renombrar la instancia
    ventana_atencion.show()
    sys.exit(app.exec())
