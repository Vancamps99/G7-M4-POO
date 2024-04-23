""" 
ABSTRACCION:
Una Clase es abstracta si tiene al menos un método abstracto.
Un Método Abstracto es aquel que solo tiene la definición del método,
además debe tener el decorador @abstractmethod.

Para crear una clase abstracta y un método abstracto, importamos:

from abc import ABC, abstractmethod

"""

from abc import ABC, abstractmethod

class Pelota(ABC):  # Clase abstracta

    # Definición del método abstracto
    @abstractmethod
    def rebotar(self, altura: int):
        pass


## Creando una subclase: una clase que nace a partir de otra clase
class PelotaDeJuguete(Pelota):
    def __init__(self):
        self.__color = "Blanco"

    # Obligación de implementar el método abstracto
    def rebotar(self, altura: int):
        pass

    def imprimir(self):
        print("Método de la subclase")

# Creación de objeto
pelotita = PelotaDeJuguete()
# TypeError: No se puede instanciar la clase abstracta PelotaDeJuguete sin una implementación para el método abstracto 'rebotar'
print(pelotita.rebotar(20))  # Se intenta llamar al método abstracto rebotar, pero arroja un error
