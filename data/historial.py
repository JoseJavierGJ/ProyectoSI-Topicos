import conexion as con

class HistorialData():
  def buscarPorFecha(self,fechaDesde, fechaHasta, tipo, documento):
    self.db = con.Conexion().conectar()
    self.cursor = self.db.cursor()
    sql = """
    SELECT D.*,T.monto as monto1, T.motivo as motivo1, T.dolares as dolares1 
    FROM transferencias T 
    LEFT JOIN depositos D ON D.tipo=T.tipo and D.documento=T.documento
    WHERE T.fecha_registro >= '{}' and T.fecha_registro <= '{}' and D.documento = '{}' and D.tipo = '{}'
    """.format(fechaDesde, fechaHasta, documento, tipo)
    res = self.cursor.execute(sql)
    data = res.fetchall()
    return data