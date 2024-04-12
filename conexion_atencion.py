import sqlite3

class Comunicacion():
  def __init__(self):
    self.conexion = sqlite3.connect('atencionCliente.db')

  def inserta_llamada(self, orden, cliente, motivo, fecha, estado):
    cursor = self.conexion.cursor()
    bd = '''INSERT INTO tabla_datos (num_orden, cliente, motivo, fecha, estado)
    VALUES('{}', '{}', '{}', '{}', '{}')'''.format(orden, cliente, motivo, fecha, estado)
    cursor.execute(bd)
    self.conexion.commit()
    cursor.close()

  def mostrar_llamadas(self):
    cursor = self.conexion.cursor()
    bd = "SELECT * FROM tabla_datos"
    cursor.execute(bd)
    registro = cursor.fetchall()
    return registro
  
  def busca_llamadas(self, numero_orden):
    cursor = self.conexion.cursor()
    bd = '''SELECT * FROM tabla_datos WHERE num_orden = {}'''.format(numero_orden)
    cursor.execute(bd)
    nombreX = cursor.fetchall()
    cursor.close()
    return nombreX
  
  # def elimina_llamadas(self, llamada):
  #   cursor = self.conexion.cursor()
  #   bd = '''DELETE FROM tabla_datos WHERE num_orden = {}'''.format(llamada)
  #   cursor.execute(bd)
  #   self.conexion.commit()
  #   cursor.close()
  def elimina_llamadas(self, llamada):
    cursor = self.conexion.cursor()
    bd = '''DELETE FROM tabla_datos WHERE num_orden = {}'''.format(llamada)
    print("Consulta SQL:", bd)  # Verifica la consulta SQL
    print("Valor de llamada:", llamada)  # Verifica el valor de llamada
    cursor.execute(bd)
    self.conexion.commit()
    cursor.close()


  def actualiza_llamadas(self, Id, orden, cliente, motivo, fecha, estado):
    cursor = self.conexion.cursor()
    bd = '''UPDATE tabla_datos SET num_orden ='{}', cliente ='{}', motivo ='{}', fecha ='{}', estado ='{}'
    WHERE id = '{}' '''.format(orden, cliente, motivo, fecha, estado, Id)
    cursor.execute(bd)
    a = cursor.rowcount
    self.conexion.commit()
    cursor.close()
    return a

  