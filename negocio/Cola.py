from queue import Queue

from .Cliente import Cliente

class Cola(Queue):
    def agregar(self, cliente:Cliente) -> None:
        return self.put(cliente)

    def estaVacia(self) -> bool:
        return self.empty()

    def siguiente(self) -> Cliente:
        return self.get()

    def size(self):
        return self.qsize()