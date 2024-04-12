import sqlite3

class Conexion():
  def __init__(self):
    # Crear base de datos
    try:
      self.con = sqlite3.connect("departamentos.db")
      self.crearTablas()
    except Exception as ex:
      print(ex)

  def crearTablas(self):
    sql_create_table1 = """ CREATE TABLE IF NOT EXISTS usuarios
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    rol TEXT,
    usuario TEXT UNIQUE,
    clave TEXT)"""
    cur = self.con.cursor()
    cur.execute(sql_create_table1)
    cur.close()
    self.crearAdmin()

  def crearAdmin(self):
    try:
      sql_insert = """ INSERT INTO usuarios values(null,'{}','{}','{}')""".format("atencion", "atencion", "123456")
      cur = self.con.cursor()
      cur.execute(sql_insert)
      self.con.commit()
    except Exception as ex:
      print("Ya se creo el usuario admin", ex)
# con = Conexion()
  def conectar(self):
    return self.con
