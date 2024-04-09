#import pelota#primera forma de importar
from pelota import Pelota #segunda forma de importar
#INSTANCIAR o CREAR OBJETO
#pelota_de_andy=pelota.Pelota()#Primera forma de importar
pelota_de_andy=Pelota()
print(pelota_de_andy) #<pelota.Pelota object at 0x000001BAD5C77D50>
print(type(pelota_de_andy))#<class 'pelota.Pelota'>
print(pelota_de_andy.forma)#redondeada
print(pelota_de_andy.material)#no contiene nada none!

#para asignarle un valor 
pelota_de_andy.material="Plastico"
print(pelota_de_andy.material)#Plastico
pelota_tenis=Pelota()
print(pelota_tenis.material)#Plastico
pelota_tenis.material="Caucho"
print(pelota_tenis.material)

print(pelota_de_andy.material)

#Metodo estatico 
#no se necesita crear un objeto para invocar a un metodo
print (Pelota.crear_rebote)#<function Pelota.crear_rebote at 0x00000295EB086D40>
print (Pelota.crear_rebote())#[5, 0, 4, 0, 3, 0, 2, 0, 1, 0]