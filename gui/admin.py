import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.uic import loadUi
from gui.atencion import AtencionWindow
from gui.empleado import EmpleadoWindow
from gui.finanzas import FinanzasWindow
from gui.gestion import GestionWindow

class AdminWindow(QMainWindow): 
    def __init__(self):
        super(AdminWindow, self).__init__()
        loadUi('gui/admin2.ui', self)  
        self.initGUI()

    def initGUI(self):
        self.btnSalir.clicked.connect(self.abrir_login)
        self.btnAtencion.clicked.connect(self.abrirAtencion)
        self.btnEmpleado.clicked.connect(self.abrirEmpleado)
        self.btnFinanzas.clicked.connect(self.abrirFinanzas)
        self.btnGestion.clicked.connect(self.abrirGestion)

    def abrirAtencion(self):
        self.atencion = AtencionWindow()
        self.atencion.show()

    def abrirEmpleado(self):
        self.empleado = EmpleadoWindow()
        self.empleado.show()

    def abrirFinanzas(self):
        self.finanzas = FinanzasWindow()

    def abrirGestion(self):
        self.gestion = GestionWindow()
        self.gestion.show()

    def abrir_login(self):
        self.close()
        from gui.login import Login
        self.login_window = Login()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana_admin = AdminWindow()
    ventana_admin.show()
    sys.exit(app.exec())
