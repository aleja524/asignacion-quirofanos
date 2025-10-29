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

class quirofano:

    def __init__(self):
        self.root = None
    
    def registrar_paciente(self, paciente):
        nuevo_nodo = BinaryTreeNode(paciente)

        if self.root is None:
            self.root == nuevo_nodo
            return
        
        q = Queue()
        q.enqueue(self.root)

        while not q.is_empty():
            actual = q.dequeue()

            if actual.leftchild is None:
                actual.leftchild = nuevo_nodo
                nuevo_nodo.parent = actual
                break
            elif actual.rightchild is None:
                actual.rightchild = nuevo_nodo
                nuevo_nodo.parent = actual
                break
            else:
                q.enqueue(actual.leftchild)
                q.enqueue(actual.rightchild)
        
        self.heap_up(nuevo_nodo)
    
    def heap_up(self, nodo):
        while nodo.parent and nodo.data < nodo.parent.data:
            nodo.data, nodo.parent.data = nodo.parent.data, nodo.data
            nodo = nodo.parent
    
    def consultar_siguiente(self):
        if self.root is not None:
            return self.root.data
        else:
            return None
        
    def programar_cirugia(self):
        if self.root is None:
            return None
        
        paciente_siguiente = self.root.data

        if self.root.leftchild is None and self.root.rightchild is None:
            self.root = None
            return paciente_siguiente
        
        q = Queue()
        q.enqueu(self.root)
        ultimo = None
        padre_ultimo = None

        while not q.is_empty():
            actual = q.enqueue()
            if actual.leftchild:
                padre_ultimo = actual
                q.enqueue(actual.leftchild)
            if actual.rightchild:
                padre_ultimo = actual
                q.enqueue(actual.rightchild)
            ultimo = actual
        
        self.root.data = ultimo.data

        if padre_ultimo.rightchild == ultimo:
            padre_ultimo.rightchild = None
        else:
            padre_ultimo.leftchild = None
        
        self.heap_down(self.root)

        print(f"{paciente_siguiente.nombre} sera llevado a cirugia")
        return paciente_siguiente
    

    def heap_down(self, nodo):
        if nodo is None:
            return

        menor = nodo 

        if nodo.leftchild and nodo.leftchild.data < menor.data:
            menor = nodo.leftchild

        if nodo.rightchild and nodo.rightchild.data < menor.data:
            menor = nodo.rightchild

        if menor != nodo:
            nodo.data, menor.data = menor.data, nodo.data
            self.heap_down(menor)