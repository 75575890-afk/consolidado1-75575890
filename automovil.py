class Automovil:
    def __init__(self, marca: str, modelo: str, velocidad_max: float,
                 nivel_combustible: float, año_fabricacion: int):
        self.marca = marca
        self.modelo = modelo
        # Se asignan con los setters para que se validen desde el inicio
        self.velocidad_max = velocidad_max
        self.nivel_combustible = nivel_combustible
        self.año_fabricacion = año_fabricacion

    @property
    def año_fabricacion(self) -> int:
        return self._año_fabricacion

    @año_fabricacion.setter
    def año_fabricacion(self, valor: int):
        if not 1886 <= valor <= 2026:
            raise ValueError(f"Año inválido ({valor}): debe estar entre 1886 y 2026")
        self._año_fabricacion = valor

    @property
    def nivel_combustible(self) -> float:
        return self._nivel_combustible

    @nivel_combustible.setter
    def nivel_combustible(self, valor: float):
        if not 0.0 <= valor <= 100.0:
            raise ValueError(f"Combustible inválido ({valor}): debe estar entre 0 y 100")
        self._nivel_combustible = valor

    @property
    def velocidad_max(self) -> float:
        return self._velocidad_max

    @velocidad_max.setter
    def velocidad_max(self, valor: float):
        if valor <= 0:
            raise ValueError(f"Velocidad inválida ({valor}): debe ser mayor a 0")
        self._velocidad_max = valor

    def tiempo_llegada(self, distancia_km: float) -> float:
        return distancia_km / self.velocidad_max

    def __str__(self) -> str:
        if self.nivel_combustible == 0:
            estado = "Vacío"
        elif self.nivel_combustible < 25:
            estado = "Reserva"
        elif self.nivel_combustible < 75:
            estado = "Medio"
        else:
            estado = "Lleno"
        return (f"{self.marca} {self.modelo} ({self.año_fabricacion}) | "
                f"Vel. máx: {self.velocidad_max} km/h | "
                f"Combustible: {self.nivel_combustible}% ({estado})")


auto = Automovil("Toyota", "Corolla", 180.0, 65.0, 2020)
print(auto)
print(f"Tiempo para 360 km: {auto.tiempo_llegada(360):.2f} horas")

auto.nivel_combustible = 20.0
print(f"Nuevo nivel de combustible: {auto.nivel_combustible}%")
print(auto)

try:
    auto.año_fabricacion = 1800
except ValueError as e:
    print(f"Error: {e}")

try:
    auto.nivel_combustible = 150
except ValueError as e:
    print(f"Error: {e}")