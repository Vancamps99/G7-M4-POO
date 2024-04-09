from te import Te

#Instanciar objetos

te1 = Te()
te2 = Te()

print(type(te1))
print(type(te2))

comp1 = type(te1)
comp2 = type(te2)

if comp1 == comp2 :
    print("Los objetos son iguales")
else:
    print("Los objetos no son del mismo tipo")