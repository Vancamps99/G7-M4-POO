from personaje import Personaje
import random

class Juego:
    def __init__(self):
        pass

    def iniciar_juego(self):
        nombre_personaje = input("Por favor, indica el nombre de tu personaje: ")
        jugador = Personaje(nombre_personaje)
        print(jugador.obtener_estado())

        orco = Personaje("Orco")
        probabilidad_ganar = Personaje.calcular_probabilidad_ganar(jugador, orco)

        print(f" !Ha aparecido un Orco.!\n"
              f"Con tu nivel actual, tienes {probabilidad_ganar * 100:.1f}% de probabilidades de ganarle al Orco.\n"
              f"Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.\n"
              f"Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.\n")

        opcion = input("Elige una acción\n1. Atacar\n2. Huir\n")

        while opcion == "1":
            resultado_ataque = "Gana" if random.uniform(0, 1) <= probabilidad_ganar else "Pierde"
            
            if resultado_ataque == "Gana":
                print("¡Le has ganado al Orco! ")
                jugador.asignar_experiencia(50)
                orco.asignar_experiencia(-30)
            else:
                print("¡El Orco te ha ganado!")
                jugador.asignar_experiencia(-30)
                orco.asignar_experiencia(50)

            print(jugador.obtener_estado())
            print(orco.obtener_estado())

            probabilidad_ganar = Personaje.calcular_probabilidad_ganar(jugador, orco)
            print(f"\nCon tu nivel actual, tienes {probabilidad_ganar * 100:.1f}% de probabilidades de ganarle al Orco.\n")
            opcion = input("¿Qué deseas hacer?\n1. Atacar\n2. Huir\n")

            if opcion == "2":
                break

        if opcion == "2":
            print("¡Has huido! El Orco ha quedado atrás.")

if __name__ == "__main__":
    juego = Juego()
    juego.iniciar_juego()
