# Importamos la clase Medicamento desde el archivo medicamento.py
from medicamento import Medicamento

# Solicitamos al usuario si desea agregar un medicamento
opcion_ingreso = int(input("¿Desea agregar un medicamento?\n1. Sí\n2. No\n"))
ingresados = []  # Lista para almacenar los medicamentos ingresados

# Ciclo para ingresar medicamentos mientras el usuario lo desee
while opcion_ingreso == 1:
    nombre = input("\nIngrese nombre del medicamento:\n")  # Solicitamos el nombre del medicamento
    stock = int(input("\nIngrese stock del medicamento:\n"))  # Solicitamos el stock del medicamento
    m = Medicamento(nombre, stock)  # Creamos un objeto de la clase Medicamento

    # Verificamos si el medicamento ya ha sido ingresado antes
    if m in ingresados:
        # Si ya existe, actualizamos el stock sumando el ingresado al existente
        indice = ingresados.index(m)
        ingresados[indice] += m
    else:
        # Si es nuevo, lo agregamos a la lista de ingresados
        ingresados.append(m)
        precio_bruto = int(input("\nIngrese precio bruto del medicamento:\n"))
        m.precio = precio_bruto  # Solicitamos y asignamos el precio bruto al medicamento

    # Mostramos los datos del medicamento ingresado
    print(f"\n***** DATOS MEDICAMENTO {m.nombre} *****")
    print(f"PRECIO BRUTO: ${m.precio_bruto}")
    if m.descuento:
        print(f"DESCUENTO: {m.descuento*100}%")
    print(f"PRECIO FINAL: ${m.precio_final}")
    print(f"STOCK: {m.stock}")

    # Solicitamos al usuario si desea ingresar otro medicamento
    print("")
    opcion_ingreso = int(input("¿Desea agregar un medicamento?\n1. Sí\n2. No\n"))

# Mostramos el total de medicamentos ingresados y sus detalles
print(f"\nLa farmacia cuenta con {len(ingresados)} medicamento(s)\n")
if len(ingresados) > 0:
    for medicamento in ingresados:
        print(medicamento)  # Imprimimos los detalles de cada medicamento
