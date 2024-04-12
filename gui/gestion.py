from PyQt6.QtWidgets import QMessageBox
from PyQt6 import uic 

class GestionWindow():
  def __init__(self):
    self.main = uic.loadUi("gui/gestion.ui")
    # self.initGUI()
    self.main.show()
