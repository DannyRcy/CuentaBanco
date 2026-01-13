"""
Define la clase CuentaBanco para la gestión básica de cuentas bancarias,
incluyendo depósitos, retiros y transferenciasy añadir una opcion para salir de la app.
"""

# pylint: disable=unused-private-member


class CuentaBanco:
    """
    Representa una cuenta bancaria con operaciones básicas y validaciones internas.
    """

    def __init__(self, titular: str, numero_cuenta: str, saldo_inicial: float = 0.0):
        """
        Inicializa una cuenta bancaria con titular, número de cuenta y saldo inicial.

        :param titular: Nombre del titular de la cuenta
        :param numero_cuenta: Identificador de la cuenta
        :param saldo_inicial: Saldo inicial de la cuenta
        """
        self.__validar_texto(titular, "El titular")
        self.__validar_texto(numero_cuenta, "El número de cuenta")
        self.__validar_saldo_inicial(saldo_inicial)

        self.__titular = titular
        self.__numero_cuenta = numero_cuenta
        self.__saldo = float(saldo_inicial)

    # ----------------------------
    # Propiedades (encapsulación)
    # ----------------------------
    @property
    def titular(self) -> str:
        """
        Devuelve el nombre del titular de la cuenta.
        """
        return self.__titular

    @property
    def numero_cuenta(self) -> str:
        """
        Devuelve el número de la cuenta bancaria.
        """
        return self.__numero_cuenta

    @property
    def saldo(self) -> float:
        """
        Devuelve el saldo actual de la cuenta.
        """
        return self.__saldo

    # ----------------------------
    # Validaciones internas
    # ----------------------------
    @staticmethod
    def __validar_texto(valor, mensaje):
        """
        Valida que un valor sea de tipo texto.

        :param valor: Valor a validar
        :param mensaje: Mensaje de error personalizado
        """
        if not isinstance(valor, str):
            raise TypeError(f"{mensaje} debe ser texto")

    @staticmethod
    def __validar_saldo_inicial(saldo):
        """
        Valida que el saldo inicial sea numérico y no negativo.

        :param saldo: Saldo inicial a validar
        """
        if not isinstance(saldo, (int, float)):
            raise TypeError("El saldo inicial debe ser numérico")
        if saldo < 0:
            raise ValueError("El saldo inicial no puede ser negativo")

    @staticmethod
    def __validar_monto(monto):
        """
        Valida que el monto sea numérico y mayor que cero.

        :param monto: Monto a validar
        """
        if not isinstance(monto, (int, float)):
            raise TypeError("El monto debe ser numérico")
        if monto <= 0:
            raise ValueError("El monto debe ser mayor que cero")

    # ----------------------------
    # Operaciones bancarias
    # ----------------------------
    def deposito_cuenta(self, monto: float) -> str:
        """
        Realiza un depósito en la cuenta.

        :param monto: Monto a depositar
        :return: Mensaje con el saldo actualizado
        """
        self.__validar_monto(monto)
        self.__saldo += monto
        return f"Depósito exitoso. Saldo actual: {self.__saldo:.2f}"

    def retiro_cuenta(self, monto: float) -> str:
        """
        Realiza un retiro de la cuenta.

        :param monto: Monto a retirar
        :return: Mensaje con el saldo actualizado
        """
        self.__validar_monto(monto)

        if monto > self.__saldo:
            raise ValueError("Saldo insuficiente")

        self.__saldo -= monto
        return f"Retiro exitoso. Saldo actual: {self.__saldo:.2f}"

    def transferencia_cuenta(self, monto: float, destino) -> str:
        """
        Transfiere un monto a otra cuenta o a un destino textual.

        :param monto: Monto a transferir
        :param destino: CuentaBanco o texto identificador del destino
        :return: Detalle de la transferencia
        """
        self.__validar_monto(monto)

        if monto > self.__saldo:
            raise ValueError("Saldo insuficiente para transferir")

        if isinstance(destino, CuentaBanco):
            saldo_antes = self.__saldo
            self.__saldo -= monto
            destino.__saldo += monto

            return (
                f"Transferencia exitosa a la cuenta {destino.numero_cuenta}\n"
                f"Saldo antes de la transferencia: {saldo_antes:.2f}\n"
                f"Saldo después de la transferencia: {self.__saldo:.2f}"
            )

        if isinstance(destino, str):
            saldo_antes = self.__saldo
            self.__saldo -= monto

            return (
                f"Transferido a: {destino}\n"
                f"Saldo antes de la transferencia: {saldo_antes:.2f}\n"
                f"Saldo después de la transferencia: {self.__saldo:.2f}"
            )

        raise TypeError("El destino debe ser texto o una cuenta válida")

    def saldo_cuenta(self) -> float:
        """
        Devuelve el saldo actual de la cuenta.
        """
        return self.__saldo
