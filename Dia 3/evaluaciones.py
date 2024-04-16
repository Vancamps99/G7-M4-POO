from pizza import Pizza

# Punto a: Mostrar los atributos de clase de la clase Pizza
print(f"El precio de las pizzas es ${Pizza.precio} y todas son de tamaño {Pizza.tamano}")

# Punto b: Validar si "salsa de tomate" está presente en la lista de ingredientes
print(Pizza.validar_elemento("salsa de tomate", ["salsa de tomate", "salsa bbq"]))

# Punto c: Crear una instancia de la clase Pizza y solicitar al usuario realizar un pedido
pizza = Pizza()
print("")
pizza.realizar_pedido()

# Verificar si la pizza creada es válida y mostrar sus ingredientes si lo es
if pizza.es_pizza_valida:
    print("")
    print("Estos son los ingredientes de su pizza:")
    print(f"Ingrediente proteico: {pizza.proteico}")
    print(f"Ingredientes vegetales: {pizza.vegetales[0]} - {pizza.vegetales[1]}")
    print(f"Tipo de masa: {pizza.masa}")
else:
    print("La pizza no es válida")
