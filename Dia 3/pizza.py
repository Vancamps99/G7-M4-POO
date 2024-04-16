from ingredientes import lista_masas, lista_proteicos, lista_vegetales

class Pizza:
    # Atributos de clase
    precio = 10000    
    tamano = "Familiar"
    
    @staticmethod
    def validar_elemento(elemento, posible_elemento):        
        return elemento.lower() in posible_elemento
    
    def realizar_pedido(self):
        # Esta variable se crea al momento de utilizar el método
        self.proteico = input("Ingrese un ingrediente proteico: Vacuno, Pollo, Carne Vegetal\n")
        
        self.vegetales = []        
        # Se agrega inmediatamente a la lista
        self.vegetales.append(input("Ingrese su primer ingrediente vegetal: Tomate, Aceitunas, Champiñones\n"))
        
        self.vegetales.append(input("Ingrese su segundo ingrediente vegetal: Tomate, Aceitunas, Champiñones\n"))
        
        self.masa = input("Ingrese tipo de masa: Tradicional, Delgada\n")
        
        self.es_pizza_valida = self.validar_elemento(self.proteico, lista_proteicos) and \
                               self.validar_elemento(self.vegetales[0], lista_vegetales) and \
                               self.validar_elemento(self.vegetales[1], lista_vegetales) and \
                               self.validar_elemento(self.masa, lista_masas)
