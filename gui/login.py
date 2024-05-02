import sys
from PyQt6 import uic 
from PyQt6.QtWidgets import QMessageBox, QLineEdit, QApplication

from data.usuario import UsuarioData
from gui.atencion import AtencionWindow
from gui.finanzas import FinanzasWindow
from gui.logistica import LogisticaWindow
from gui.gestion import GestionWindow
from model.usuario import Usuario

class Login():
  def __init__(self):
    self.login = uic.loadUi("gui/login.ui")
    self.initGUI()
    self.login.check_view_password.toggled.connect(self.mostrar_contrasena)
    self.login.lblMensaje.setText("")
    self.login.exec()

    
  def ingresar(self):
    if len(self.login.txtUsuario.text()) < 2:
      self.login.lblMensaje.setText("Ingrese un usuario válido")
      self.login.txtUsuario.setFocus()
    elif len(self.login.txtClave.text()) < 3:
      self.login.lblMensaje.setText("Ingrese un contraseña válido")
      self.login.txtClave.setFocus()
    else:
      self.login.lblMensaje.setText("")
      usu = Usuario(usuario=self.login.txtUsuario.text(), clave=self.login.txtClave.text())
      usuData = UsuarioData()
      res = usuData.login(usu)
      if res:
        # Determinar el rol del usuario
        rol = usuData.obtener_rol(usu)
        # Mostrar la ventana correspondiente al rol
        if rol == 'gestion':
          self.gestion = GestionWindow()
          self.gestion.show() 
        elif rol == 'logistica':
          self.logistica = LogisticaWindow()
        elif rol == 'finanzas':
          self.finanzas = FinanzasWindow()
        elif rol == 'atencion':
          self.atencion = AtencionWindow()
          self.atencion.show() 
        else:
          QMessageBox.warning(self.login, "Error", "Rol no válido")
          return
        self.login.close() #hide
      else:
        self.login.lblMensaje.setText("Datos de acceso incorrectos")

  def initGUI(self):
    self.login.btnAcceder.clicked.connect(self.ingresar)

  def mostrar_contrasena(self, clicked):
    if clicked:
        self.login.txtClave.setEchoMode(QLineEdit.EchoMode.Normal)
    else:
        self.login.txtClave.setEchoMode(QLineEdit.EchoMode.Password)
  
  
if __name__  == '__main__':
    app = QApplication(sys.argv)
    ventana_Login = Login()
    ventana_Login.show()
    sys.exit(app.exec())

