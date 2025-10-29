from arbol import *
from queue import *

class paciente:
    orden = 0

    def __init__(self, id, nombre, nivel_emergencia):
        paciente.orden += 1
        self.id = id
        self.nombre = nombre
        self.nivel_emergencia = nivel_emergencia
        self.orden_llegada = paciente.orden
    
    def __lt__(self, other):
        if self.nivel_emergencia == other.nivel_emergencia:
            return self.orden_llegada < other.orden_llegada
        return self.nivel_emergencia < other.nivel_emergencia
    
    def __str__(self):
        return  f"{self.nombre} [PRIORIDAD: {self.nivel_emergencia} - LLEGADA: {self.orden_llegada}]"