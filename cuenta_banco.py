class CuentaBanco:
    def __init__(self, titular: str, numero_cuenta: str, saldo_inicial: float = 0.0):
        if not isinstance(titular, str):
            raise TypeError("El titular debe ser texto")

        if not isinstance(numero_cuenta, str):
            raise TypeError("El número de cuenta debe ser texto")

        if not isinstance(saldo_inicial, (int, float)):
            raise TypeError("El saldo inicial debe ser numérico")

        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo")

        self.__titular = titular
        self.__numero_cuenta = numero_cuenta
        self.__saldo = float(saldo_inicial)

    # ----------------------------
    # Validación interna
    # ----------------------------
    def __validar_monto(self, monto):
        if not isinstance(monto, (int, float)):
            raise TypeError("El monto debe ser numérico")
        if monto <= 0:
            raise ValueError("El monto debe ser mayor que cero")

    # ----------------------------
    # Operaciones bancarias
    # ----------------------------
    def deposito_cuenta(self, monto: float):
        self.__validar_monto(monto)
        self.__saldo += monto
        return f"Depósito exitoso. Saldo actual: {self.__saldo:.2f}"

    def retiro_cuenta(self, monto: float):
        self.__validar_monto(monto)

        if monto > self.__saldo:
            raise ValueError("Saldo insuficiente")

        self.__saldo -= monto
        return f"Retiro exitoso. Saldo actual: {self.__saldo:.2f}"

    def transferencia_cuenta(self, monto: float, destino: str):
        self.__validar_monto(monto)

        if not isinstance(destino, str):
            raise TypeError("El destino debe ser texto")

        if monto > self.__saldo:
            raise ValueError("Saldo insuficiente para transferir")

        saldo_antes = self.__saldo
        self.__saldo -= monto

        return (
            f"Transferido a: {destino}\n"
            f"Saldo antes de la transferencia: {saldo_antes:.2f}\n"
            f"Saldo después de la transferencia: {self.__saldo:.2f}"
        )

    def saldo_cuenta(self):
        return self.__saldo
