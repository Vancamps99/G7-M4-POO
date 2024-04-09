from te import Te


tipo_te = int(input("Ingrese el tipo de Té que desee una recomendación: 1. Té Negro, 2. Té Verde, 3. Agua de Hierbas\nIngrese el valor numerico > "))
Te.recomendacion(tipo_te)
print("")

gramos = int(input("Ingrese el tipo de formato que quiere: 1. 300g 2. 500g\n Ingrese el valor numerico > "))
Te.precio_gramos(gramos)