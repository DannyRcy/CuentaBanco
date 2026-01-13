from cuenta_banco import CuentaBanco

def mostrar_menu():
    print("\n===== MENÚ BANCO =====")
    print("1. Depósito")
    print("2. Retiro")
    print("3. Transferencia")
    print("4. Consulta de saldo")
    print("5. Salir")


def main():
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
                destino = input(
                    "Ingrese nombre o número de cuenta destino: "
                )
                monto = float(input("Ingrese monto a transferir: "))
                print(cuenta.transferencia_cuenta(monto, destino))

            elif opcion == 4:
                print(f"Saldo actual: {cuenta.saldo_cuenta():.2f}")

            elif opcion == 5:
                print("Gracias por usar el sistema bancario.")
                break

            else:
                print("Opción inválida")

        except ValueError as ve:
            print(f"Error: {ve}")
        except TypeError as te:
            print(f"Error: {te}")
        except Exception as e:
            print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()
