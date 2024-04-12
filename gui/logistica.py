from PyQt6 import uic 
from PyQt6.QtWidgets import QMessageBox

class LogisticaWindow():
  def __init__(self):
    self.main = uic.loadUi("gui/logistica.ui")
    self.main.show()