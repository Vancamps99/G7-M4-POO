from medicamento import Medicamento

# Instancia de objetos
paracetamol = Medicamento()
aspirina = Medicamento()

print(paracetamol)
print(aspirina)

# Establecer el IVA del paracetamol
#paracetamol.IVA = 0.25
print(paracetamol.IVA)
print(aspirina.IVA)  # 

precio = int(input("Ingrese el precio a validar: "))

# Llamado a un método estático
es_valido = Medicamento.validar_mayor_a_cero(precio)

if es_valido:
    print("El precio ingresado es válido")
else:
    print("El precio ingresado no es válido")

# Se verifica si todas las instancias tienen los mismos valores de IVA y descuento
if paracetamol.IVA == aspirina.IVA and paracetamol.descuento == aspirina.descuento:
    print("Todas las instancias tienen los mismos valores de IVA y descuento")
    print("El valor del IVA es", paracetamol.IVA)
    print("El valor de descuento es", paracetamol.descuento)
