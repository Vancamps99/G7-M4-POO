import random

class Personaje:
    def __init__(self, nombre: str):
        # Constructor de la clase Personaje.
        # Inicializa el nombre, nivel y experiencia del personaje.
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

    def obtener_estado(self):
        # Método para obtener el estado del personaje.
        # Devuelve una cadena con el nombre, nivel y experiencia del personaje.
        return f"NOMBRE: {self.nombre}, NIVEL: {self.nivel}, EXPERIENCIA: {self.experiencia}"

    def asignar_experiencia(self, experiencia: int):
        # Método para asignar experiencia al personaje.
        # Ajusta el nivel y la experiencia del personaje según la cantidad de experiencia recibida.
        nueva_experiencia = self.experiencia + experiencia
        
        # Ajuste del nivel si se superan los 100 puntos de experiencia.
        if nueva_experiencia >= 100:
            niveles_subir = nueva_experiencia // 100
            self.nivel += niveles_subir
            nueva_experiencia %= 100
        
        # Ajuste del nivel si la experiencia es negativa.
        while nueva_experiencia < 0 and self.nivel > 1:
            self.nivel -= 1
            nueva_experiencia += 100

        # Actualización de la experiencia del personaje.
        self.experiencia = max(0, nueva_experiencia)

    def __gt__(self, other):
        # Método especial para comparar si un personaje es mayor que otro basado en su nivel.
        # Devuelve True si el nivel del personaje actual es mayor que el nivel del otro personaje, False en caso contrario.
        return self.nivel > other.nivel

    def __lt__(self, other):
        # Método especial para comparar si un personaje es menor que otro basado en su nivel.
        # Devuelve True si el nivel del personaje actual es menor que el nivel del otro personaje, False en caso contrario.
        return self.nivel < other.nivel

    @staticmethod
    def calcular_probabilidad_ganar(jugador, orco):
        # Método estático para calcular la probabilidad de ganar del jugador contra el Orco.
        # Devuelve la probabilidad de ganar, que varía según la diferencia de nivel entre el jugador y el Orco.
        if jugador > orco:
            return 0.66
        elif jugador < orco:
            return 0.33
        else:
            return 0.5
