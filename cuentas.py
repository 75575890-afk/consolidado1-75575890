class CuentaBancaria:
    def __init__(self, numero_cuenta: str, titular: str):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.__saldo = 0.0

    def _modificar_saldo(self, nuevo_saldo: float):
        """Permite a las clases hijas actualizar el saldo privado."""
        self.__saldo = nuevo_saldo

    def depositar(self, monto: float):
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