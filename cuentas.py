class CuentaBancaria:
    def __init__(self, numero_cuenta: str, titular: str):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.__saldo = 0.0

    def _modificar_saldo(self, nuevo_saldo: float):
        """Permite a las clases hijas actualizar el saldo privado."""
        self.__saldo = nuevo_saldo

    def depositar(self, monto: float):
        # HOTFIX: se valida que el monto de depósito sea positivo
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser mayor a 0")
        self.__saldo += monto
        
    def retirar(self, monto: float):
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor a 0")
        if monto > self.__saldo:
            raise ValueError("Saldo insuficiente")
        self.__saldo -= monto

    def consultar_saldo(self) -> float:
        return self.__saldo

    def __str__(self) -> str:
        return (f"Cuenta: {self.numero_cuenta} | Titular: {self.titular} | "
                f"Saldo: S/ {self.__saldo:.2f}")
    

class CuentaAhorros(CuentaBancaria):
    def __init__(self, numero_cuenta: str, titular: str, tasa_interes: float):
        super().__init__(numero_cuenta, titular)
        self.tasa_interes = tasa_interes

    def calcular_interes(self) -> float:
        return self.consultar_saldo() * self.tasa_interes / 100

    def __str__(self) -> str:
        return (f"{super().__str__()} | Tasa: {self.tasa_interes}% | "
                f"Interés anual: S/ {self.calcular_interes():.2f}")
    

class CuentaCorriente(CuentaBancaria):
    def __init__(self, numero_cuenta: str, titular: str, limite_sobregiro: float):
        super().__init__(numero_cuenta, titular)
        self.limite_sobregiro = limite_sobregiro

    def retirar(self, monto: float):
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor a 0")
        if monto > self.consultar_saldo() + self.limite_sobregiro:
            raise ValueError("El retiro excede el saldo más el límite de sobregiro")
        self._modificar_saldo(self.consultar_saldo() - monto)

    def permite_sobregiro(self) -> bool:
        return self.consultar_saldo() < 0

    def __str__(self) -> str:
        return f"{super().__str__()} | Límite sobregiro: S/ {self.limite_sobregiro:.2f}"


ahorros = CuentaAhorros("AH-001", "Eduardo Puma", 4.5)
ahorros.depositar(1000)
ahorros.retirar(200)
print(ahorros)
print(f"Interés anual calculado: S/ {ahorros.calcular_interes():.2f}")

corriente = CuentaCorriente("CC-001", "Eduardo Puma", 500)
corriente.depositar(300)
corriente.retirar(600)
print(corriente)
print(f"¿Está en sobregiro?: {corriente.permite_sobregiro()}")

try:
    corriente.retirar(1000)
except ValueError as e:
    print(f"Error: {e}")

try:
    ahorros.depositar(-50)
except ValueError as e:
    print(f"Error: {e}")