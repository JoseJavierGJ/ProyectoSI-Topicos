import conexion as con

class CiudadData():
  def listaCiudades(self):
    self.db = con.Conexion().conectar()
    self.cursor = self.db.cursor()
    res = self.cursor.execute("SELECT * FROM ciudades order by nombre")
    ciudades = res.fetchall()
    return ciudades
