"""
Aplicación de consola para interactuar con una cuenta bancaria,
permitiendo depósitos, retiros, transferencias y consultas de saldo.
"""

from cuenta_banco import CuentaBanco


def mostrar_menu():
    """
    Muestra el menú principal del sistema bancario en consola.
    """
    print("\n===== MENÚ BANCO =====")
    print("1. Depósito")
    print("2. Retiro")
    print("3. Transferencia")
    print("4. Consulta de saldo")
    print("5. Salir")


def main():
    """
    Función principal que ejecuta el sistema bancario interactivo.
    """
    cuenta = CuentaBanco("Titular Principal", "001", 0.0)

    while True:
        mostrar_menu()

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                monto = float(input("Ingrese monto a depositar: "))
                print(cuenta.deposito_cuenta(monto))

            elif opcion == 2:
                monto = float(input("Ingrese monto a retirar: "))
                print(cuenta.retiro_cuenta(monto))

            elif opcion == 3:
                destino = input("Ingrese nombre o número de cuenta destino: ")
                monto = float(input("Ingrese monto a transferir: "))
                print(cuenta.transferencia_cuenta(monto, destino))

            elif opcion == 4:
                print(f"Saldo actual: {cuenta.saldo_cuenta():.2f}")

            elif opcion == 5:
                print("Gracias por usar el sistema bancario.")
                break

            else:
                print("Opción inválida. Intente nuevamente.")

        except ValueError as error:
            print(f"Error de valor: {error}")
        except TypeError as error:
            print(f"Error de tipo: {error}")
        except Exception as error:  # pylint: disable=broad-exception-caught
            print(f"Error inesperado: {error}")


if __name__ == "__main__":
    main()
