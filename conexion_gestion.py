import sqlite3

class Comunicacion():
  def __init__(self):
    self.conexion = sqlite3.connect('gestion.db')

  def inserta_llamada(self, tarjeta, cliente, tipo_tarjeta, saldo, estado):
    cursor = self.conexion.cursor()
    bd = '''INSERT INTO tabla_datos (tarjeta, cliente, tipo_tarjeta, saldo, estado)
    VALUES('{}', '{}', '{}', '{}', '{}')'''.format(tarjeta, cliente, tipo_tarjeta, saldo, estado)
    cursor.execute(bd)
    self.conexion.commit()
    cursor.close()

  def mostrar_llamadas(self):
    cursor = self.conexion.cursor()
    bd = "SELECT * FROM tabla_datos"
    cursor.execute(bd)
    registro = cursor.fetchall()
    return registro
  
  def busca_llamadas(self, numero_tarjeta):
    cursor = self.conexion.cursor()
    bd = '''SELECT * FROM tabla_datos WHERE tarjeta = {}'''.format(numero_tarjeta)
    cursor.execute(bd)
    resultados = cursor.fetchall()
    cursor.close()
    return resultados

  
  # def elimina_llamadas(self, llamada):
  #   cursor = self.conexion.cursor()
  #   bd = '''DELETE FROM tabla_datos WHERE num_orden = {}'''.format(llamada)
  #   cursor.execute(bd)
  #   self.conexion.commit()
  #   cursor.close()
  def elimina_llamadas(self, llamada):
      cursor = self.conexion.cursor()
      bd = '''DELETE FROM tabla_datos WHERE tarjeta = {}'''.format(llamada)
      print("Consulta SQL:", bd) 
      print("Valor de llamada:", llamada) 
      cursor.execute(bd)
      self.conexion.commit()
      cursor.close()


  def actualiza_llamadas(self, Id, tarjta, cliente, tipo_tarjeta, saldo, estado):
    cursor = self.conexion.cursor()
    bd = '''UPDATE tabla_datos SET tarjeta ='{}', cliente ='{}', tipo_tarjeta ='{}', saldo ='{}', estado ='{}'
    WHERE id = '{}' '''.format( tarjta, cliente, tipo_tarjeta, saldo, estado, Id)
    cursor.execute(bd)
    a = cursor.rowcount
    self.conexion.commit()
    cursor.close()
    return a


  