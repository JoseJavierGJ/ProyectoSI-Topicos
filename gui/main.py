from PyQt6 import uic 
from PyQt6.QtWidgets import QMessageBox

class MainWindow():
  def __init__(self):
    self.main = uic.loadUi("gui/main.ui")
    self.initGUI()
    # self.main.showMaximized()
    self.main.show()

  def initGUI(self):
    self.main.btnRegistrar_Transferencias_2.clicked.connect(self.abrirRegistro)
    self.main.btnRegistrar_Transferencias.triggered.connect(self.abrirRegistro)
    self.registro = uic.loadUi("gui/registro.ui")

  def abrirRegistro(self):
    self.registro.btnRegistrar.clicked.connect(self.registrarTransaccion)
    self.registro.show()

  def registrarTransaccion(self):
    if self.registro.cbTipo.currentText() == "--- Seleccione una opción":
      mBox = QMessageBox()
      mBox.setText("Debe seleccionar el tipo de documento")
      mBox.exec()
      self.registro.cbTipo.setFocus()
    elif len(self.registro.txtDocumento.text()) < 4:
      mBox = QMessageBox()
      mBox.setText("Debe de ingresar un documento válido")
      mBox.exec()
      self.registro.txtDocumento.setFocus()
    elif self.registro.cbMotivo.currentText() == "--- Seleccione una opción":
      mBox = QMessageBox()
      mBox.setText("Debe seleccionar el motivo")
      mBox.exec()
      self.registro.cbMotivo.setFocus()
    elif not self.registro.txtMonto.text().isnumeric():
      mBox = QMessageBox()
      mBox.setText("Debe de ingresar un monto válido")
      mBox.exec()
      self.registro.txtMonto.setText("0")
      self.registro.txtMonto.setFocus()
