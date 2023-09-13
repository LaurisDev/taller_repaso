from dataclasses import dataclass


@dataclass
class Elemento:
    nombre = str

    def __eq__(self, other):
        return Elemento.nombre == Elemento.nombre


class Conjunto:
    contador: int = 0

    def __init__(self, nombre):
        self.elementos: list[Elemento] = []
        self.nombre = nombre
        Conjunto.contador += 1
        self._id = Conjunto.contador

    @property
    def __id(self):
        return self._id

    def contiene(self, elemento) -> bool:
        elemento: elemento = Elemento()
        if isinstance(elemento, Elemento):
            for elemento in self.elementos:
                if elemento.nombre == elemento.nombre:
                    return True
        return False
    def agregar_elemento(self):
        pass



