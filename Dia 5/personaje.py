import random

class Personaje:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

    def obtener_estado(self):
        return f"NOMBRE: {self.nombre}, NIVEL: {self.nivel}, EXPERIENCIA: {self.experiencia}"

    def asignar_experiencia(self, experiencia: int):
        nueva_experiencia = self.experiencia + experiencia
        
        if nueva_experiencia >= 100:
            niveles_subir = nueva_experiencia // 100
            self.nivel += niveles_subir
            nueva_experiencia %= 100
        
        while nueva_experiencia < 0 and self.nivel > 1:
            self.nivel -= 1
            nueva_experiencia += 100

        self.experiencia = max(0, nueva_experiencia)

    def __gt__(self, other):
        return self.nivel > other.nivel

    def __lt__(self, other):
        return self.nivel < other.nivel

    @staticmethod
    def calcular_probabilidad_ganar(jugador, orco):
        if jugador > orco:
            return 0.66
        elif jugador < orco:
            return 0.33
        else:
            return 0.5
