from PyQt6 import uic 
from PyQt6.QtWidgets import QMessageBox

from model.movimientos import Transferencia
from data.transferencia import TransferenciaData

class MainWindow():
  def __init__(self):
    self.main = uic.loadUi("gui/main.ui")
    self.initGUI()
    # self.main.showMaximized()
    self.main.show()

  def initGUI(self):
    self.main.btnRegistrar_Transferencias_2.clicked.connect(self.abrirRegistro)
    self.main.btnRegistrar_Transferencias.triggered.connect(self.abrirRegistro)
    self.main.btnReportar_Tranferencia_2.clicked.connect(self.abrirDeposito)
    self.main.btnReportar_Tranferencia.triggered.connect(self.abrirDeposito)
    self.registro = uic.loadUi("gui/registro.ui")
    self.deposito = uic.loadUi("gui/deposito.ui")

  def abrirRegistro(self):
    self.registro.btnRegistrar.clicked.connect(self.registrarTransferencia)
    self.registro.show()

  def abrirDeposito(self):
    self.deposito.btnRegistrar.clicked.connect(self.registrarTransferencia)
    self.deposito.show()


  ############## Tranferencias ##############
  def registrarTransferencia(self):
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
    else:
      transferencia = Transferencia(
        tipo = self.registro.cbTipo.currentText(),
        documento = self.registro.txtDocumento.text(),
        monto = float(self.registro.txtMonto.text()),
        motivo = self.registro.cbMotivo.currentText(),
        dolares = self.registro.checkDolares.isChecked(),
        internacional = self.registro.checkInternacional.isChecked() 
      )
      objData = TransferenciaData()
      mBox = QMessageBox()
      if objData.registrar(info = transferencia):
        self.limpiarCamposTransferencias()
        mBox.setText("Transferencia registrada")
      else:
        mBox.setText("Transferencia no registrada")
      mBox.exec()

  def limpiarCamposTransferencias(self):
    self.registro.cbTipo.setCurrentIndex(0)
    self.registro.cbMotivo.setCurrentIndex(0)
    self.registro.txtDocumento.setText("")
    self.registro.txtMonto.setText("0")
    self.registro.checkDolares.setChecked(False)
    self.registro.checkInternacional.setChecked(False)
    self.registro.txtDocumento.setFocus()

  ############## Tranferencias ##############

