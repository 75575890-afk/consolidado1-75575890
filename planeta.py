import math


class Planeta:
    def __init__(self, nombre: str, masa: float, radio: float,
                 distancia_al_sol: float, tiene_vida: bool = False):
        self.nombre = nombre
        self.masa = masa
        self.radio = radio
        self.distancia_al_sol = distancia_al_sol
        self.tiene_vida = tiene_vida
        
    def calcular_densidad(self) -> float:
        volumen = (4 / 3) * math.pi * self.radio ** 3
        return self.masa / volumen

    def es_planeta_exterior(self) -> bool:
        return self.distancia_al_sol > 5.2