# Importamos la clase Personaje del módulo personaje.py y el módulo random para generar números aleatorios.
from personaje import Personaje
import random

# Definimos la clase Juego.
class Juego:
    # El método constructor __init__ no tiene ningún parámetro ya que no es necesario inicializar atributos en este caso.
    def __init__(self):
        pass

    # Método para iniciar el juego.
    def iniciar_juego(self):
       
        nombre_personaje = input("Por favor, indica el nombre de tu personaje: ")
        # Creamos un objeto de la clase Personaje con el nombre proporcionado por el usuario.
        jugador = Personaje(nombre_personaje)
        # Mostramos en pantalla el estado inicial del personaje del jugador.
        print(jugador.obtener_estado())

        # Creamos un objeto de la clase Personaje para representar al orco.
        orco = Personaje("Orco")
        # Calcular la probabilidad de ganar del jugador contra el orco.
        probabilidad_ganar = Personaje.calcular_probabilidad_ganar(jugador, orco)

        # Mostramos en pantalla la situación inicial del juego, incluyendo la probabilidad de ganar contra el Orco.
        print(f"¡Ha aparecido un Orco!\n"
              f"Con tu nivel actual, tienes {probabilidad_ganar * 100:.1f}% de probabilidades de ganarle al Orco.\n"
              f"Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.\n"
              f"Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.\n")

        # Solicitamos al usuario que elija una acción: atacar o huir.
        opcion = input("Elige una acción\n1. Atacar\n2. Huir\n")

        # Comenzamos un bucle mientras el jugador elija atacar.
        while opcion == "1":
            # Generamos resultado de ataque aleatorio.
            resultado_ataque = "Gana" if random.uniform(0, 1) <= probabilidad_ganar else "Pierde"
            
            #resultado del ataque y a estado actual  de los personajes.
            if resultado_ataque == "Gana":
                print("¡Le has ganado al Orco! ")
                jugador.asignar_experiencia(50)
                orco.asignar_experiencia(-30)
            else:
                print("¡El Orco te ha ganado!")
                jugador.asignar_experiencia(-30)
                orco.asignar_experiencia(50)

            # estados actualizados de los personajes.
            print(jugador.obtener_estado())
            print(orco.obtener_estado())

            # nueva probabilidad de ganar contra el Orco.
            probabilidad_ganar = Personaje.calcular_probabilidad_ganar(jugador, orco)
            print(f"\nCon tu nivel actual, tienes {probabilidad_ganar * 100:.1f}% de probabilidades de ganarle al Orco.\n")

          
            opcion = input("¿Qué deseas hacer?\n1. Atacar\n2. Huir\n")

            #  salir del bucle.
            if opcion == "2":
                break

       
        if opcion == "2":
            print("¡Has huido! El Orco ha quedado atrás.")

# Bloque principal donde creamos un objeto de la clase Juego y llamamos al método iniciar_juego para comenzar el juego.
if __name__ == "__main__":
    juego = Juego()
    juego.iniciar_juego()
