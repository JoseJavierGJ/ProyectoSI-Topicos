class Transferencia():
  def __init__(self, tipo:str, documento:str, motivo:float, monto:int, dolares:bool, internacional:bool):
    self._tipo = tipo
    self._documento = documento
    self._motivo = motivo
    self._monto = monto
    self._dolares = dolares
    self._internacional = internacional