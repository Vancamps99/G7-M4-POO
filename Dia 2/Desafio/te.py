class Te():
    tipo = ["Negro", "Verde", "Hierba"]
    caducidad = 365
    preparacion = [3, 5, 6]
    formato = [300, 500]
    precio = [3000, 5000]
    
    @staticmethod
    def recomendacion(tipo_te):
        if tipo_te == 1:
            print(f"El Té {Te.tipo[0]} se prepara durante {Te.preparacion[0]} minutos y se recomienda beberlo en la mañana")
        elif tipo_te == 2:
            print(f"El Té {Te.tipo[1]} se prepara durante {Te.preparacion[1]} minutos y se recomienda beberlo en la tarde")
        elif tipo_te == 3:
            print(f"El agua de {Te.tipo[2]} se preapara durante {Te.preparacion[2]} min y se recomienda beberlo al atardecer")
        else:
            print("Por favor ingrese un número de la lista")
        
    @staticmethod
    
    def precio_gramos(gramos):
        if gramos == 1:
            print(f"El precio por {Te.formato[0]} gramos es de {Te.precio[0]} pesos")
        elif gramos == 2:
            print(f"El precio por {Te.formato[1]} gramos es de {Te.precio[1]} pesos")
        else:
            print("Por favor ingrese un número de la lista")