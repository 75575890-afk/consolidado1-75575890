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

    
    def __str__(self) -> str:
        tipo = "exterior" if self.es_planeta_exterior() else "interior"
        vida = "Sí" if self.tiene_vida else "No"
        return (f"Planeta: {self.nombre} | Densidad: {self.calcular_densidad():.2f} kg/m³ | "
                f"Tipo: {tipo} | Tiene vida: {vida}")


if __name__ == "__main__":
    tierra = Planeta("Tierra", 5.972e24, 6.371e6, 1.0, True)
    saturno = Planeta("Saturno", 5.683e26, 5.8232e7, 9.58)
    print(tierra)
    print(saturno)