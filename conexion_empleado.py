import sqlite3

class Comunicacion:
  def __init__(self):
    self.conexion = sqlite3.connect('empleados.db')

  def inserta_llamada(self, num_empleado, nombre, genero, fecha_admision, oficio, telefono, num_oficina, salario, comision):
    cursor = self.conexion.cursor()
    bd = '''INSERT INTO tabla_datos (num_empleado, nombre, genero, fecha_admision, oficio, telefono, num_oficina, salario, comision)
    VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')'''.format(num_empleado, nombre, genero, fecha_admision, oficio, telefono, num_oficina, salario, comision)
    cursor.execute(bd)
    self.conexion.commit()
    cursor.close()

  def mostrar_llamadas(self):
    cursor = self.conexion.cursor()
    bd = "SELECT * FROM tabla_datos"
    cursor.execute(bd)
    registro = cursor.fetchall()
    return registro

  def busca_llamadas(self, num_empleado):
    cursor = self.conexion.cursor()
    bd = '''SELECT * FROM tabla_datos WHERE num_empleado = {}'''.format(num_empleado)
    cursor.execute(bd)
    resultado = cursor.fetchall()
    cursor.close()
    return resultado

  def elimina_llamadas(self, num_empleado):
    cursor = self.conexion.cursor()
    bd = '''DELETE FROM tabla_datos WHERE num_empleado = {}'''.format(num_empleado)
    cursor.execute(bd)
    self.conexion.commit()
    cursor.close()

  def actualiza_llamadas(self, Id, num_empleado, nombre, genero, fecha_admision, oficio, telefono, num_oficina, salario, comision):
    cursor = self.conexion.cursor()
    bd = '''UPDATE tabla_datos SET nombre ='{}', genero ='{}', fecha_admision ='{}', oficio ='{}', telefono ='{}', num_oficina ='{}', salario ='{}', comision ='{}'
    WHERE num_empleado = '{}' '''.format(nombre, genero, fecha_admision, oficio, telefono, num_oficina, salario, comision, num_empleado, Id)
    cursor.execute(bd)
    filas_modificadas = cursor.rowcount
    self.conexion.commit()
    cursor.close()
    return filas_modificadas
