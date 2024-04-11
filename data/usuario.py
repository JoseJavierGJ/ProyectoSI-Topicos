import conexion as con
from model.usuario import Usuario

class UsuarioData():
  def login(self, usuario:Usuario):
    self.db = con.Conexion().conectar()
    self.cursor = self.db.cursor()
    res = self.cursor.execute("SELECT * FROM usuarios WHERE usuario='{}' AND clave='{}'".format(usuario._usuario,usuario._clave))
    fila = res.fetchone()
    if fila:
      usuario = Usuario(rol=fila[1], usuario=fila[2])
      self.cursor.close()
      self.db.close()
      return usuario
    else:
      self.cursor.close()
      self.db.close()
      return None
    
  def obtener_rol(self, usuario: Usuario):
    self.db = con.Conexion().conectar()
    self.cursor = self.db.cursor()
    res = self.cursor.execute("SELECT rol FROM usuarios WHERE usuario='{}'".format(usuario._usuario))
    fila = res.fetchone()
    if fila:
      rol = fila[0]
      print("Rol del usuario:", rol)
      self.cursor.close()
      self.db.close()
      return rol
    else:
      self.cursor.close()
      self.db.close()
      return None