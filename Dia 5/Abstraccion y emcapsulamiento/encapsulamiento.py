class Auto:
    __color = "Blanco"  # Atributo de clase privado

    def __cambiar_color(self, color):  # Método privado para cambiar el color
        print("Nuevo color:", color)
        self.__color = color

    def imprimir_estado(self, nuevo_color):  # Método para imprimir el estado y cambiar el color
        print(self.__color)  # Llamada al atributo de clase privado
        self.__cambiar_color(nuevo_color)  # Llamada al método privado para cambiar el color
        print(self.color)  # Llamada al getter para obtener el color actual

    # Getter para obtener el valor del color
    @property
    def color(self):
        return self.__color

# Creación de objeto de la clase Auto
nissan = Auto()

# Imprimiendo el color directamente (acceso al atributo de clase privado)
print(nissan._Auto__color)
print("")

# Intento de acceso a atributo de clase privado directamente (genera un error)
# print(nissan.__color)  # AttributeError: 'Auto' object has no attribute '__color'

# Intento de acceso a atributo de clase privado desde la clase (genera un error)
# print(Auto.__color)  # AttributeError: type object 'Auto' has no attribute '__color'

# Intento de llamar al método privado (genera un error)
# nissan.cambiar_color("Negro")  # AttributeError: 'Auto' object has no attribute 'cambiar_color'

# Llamada al método imprimir_estado para cambiar el color e imprimir el estado actual
nissan.imprimir_estado("Negro")
print("")

# Llamada al getter para obtener el color actual
print(nissan.color)

# Imprimiendo el color directamente (acceso al atributo de clase privado)
print(nissan._Auto__color)
