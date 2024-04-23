class Medicamento():
    # IVA que se aplica a los medicamentos, es como el impuesto que les agregamos
    IVA = 0.18

    # Al crear un Medicamento, le damos un nombre y opcionalmente una cantidad en stock
    def __init__(self, nombre: str, stock: int = 0):
        # Guardamos el nombre y la cantidad de este medicamento
        self.nombre = nombre
        self.stock = stock
        # Estos son los precios, inicialmente en 0 porque no los conocemos aún
        self.precio_bruto = 0
        self.precio_final = 0.0
        # Descuento inicialmente en 0, si hay algún descuento, se actualizará después
        self.descuento = 0.0

    # Método estático que verifica si un número es mayor que cero
    @staticmethod
    def validar_mayor_a_cero(numero: int):
        return numero > 0

    # Getter para obtener el precio final del medicamento
    @property
    def precio(self):
        return self.precio_final

    # Setter para establecer el precio del medicamento y calcular el precio final con impuestos y descuentos
    @precio.setter
    def precio(self, precio_bruto: int):
        # Si el precio bruto es válido (mayor que cero)
        if self.validar_mayor_a_cero(precio_bruto):
            # Guardamos el precio bruto
            self.precio_bruto = precio_bruto
            # Calculamos el precio final añadiendo el IVA
            self.precio_final = precio_bruto + precio_bruto * self.IVA
            # Aplicamos descuentos según el precio final
            if self.precio_final >= 10000 and self.precio_final < 20000:
                self.descuento = 0
