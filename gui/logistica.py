from PyQt6 import uic 
from PyQt6.QtWidgets import QMessageBox
from PyQt6.uic import loadUi

class LogisticaWindow():
  def __init__(self):
    super(LogisticaWindow, self).__init__()
    loadUi('gui/atencion.ui', self)