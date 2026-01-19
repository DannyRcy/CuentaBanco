import unittest
from src.logica.cuenta_banco import CuentaBanco


class TestCuentaBanco(unittest.TestCase):
    """
    Pruebas unitarias para la clase CuentaBanco
    """

    # ----------------------------
    # SETUP / TEARDOWN
    # ----------------------------
    def setUp(self):
        """Arrange: crear cuentas de prueba"""
        self.cuenta = CuentaBanco("Juan Perez", "123", 100.0)
        self.cuenta_destino = CuentaBanco("Maria Lopez", "456", 50.0)

    def tearDown(self):
        self.cuenta = None
        self.cuenta_destino = None

    # ----------------------------
    # CONSTRUCTOR
    # ----------------------------
    def test_crearCuenta_datosValidos_creaCuentaCorrectamente(self):
        self.assertEqual(self.cuenta.titular, "Juan Perez")
        self.assertEqual(self.cuenta.numero_cuenta, "123")
        self.assertEqual(self.cuenta.saldo, 100.0)

    def test_crearCuenta_saldoNegativo_lanzaValueError(self):
        with self.assertRaises(ValueError):
            CuentaBanco("Pedro", "999", -50)

    # ----------------------------
    # DEPÓSITO
    # ----------------------------
    def test_deposito_montoValido_incrementaSaldo(self):
        mensaje = self.cuenta.deposito_cuenta(50)
        self.assertEqual(self.cuenta.saldo, 150.0)
        self.assertIn("Depósito exitoso", mensaje)

    def test_deposito_montoCero_lanzaValueError(self):
        with self.assertRaises(ValueError):
            self.cuenta.deposito_cuenta(0)

    # ----------------------------
    # RETIRO
    # ----------------------------
    def test_retiro_montoValido_reduceSaldo(self):
        mensaje = self.cuenta.retiro_cuenta(40)
        self.assertEqual(self.cuenta.saldo, 60.0)
        self.assertIn("Retiro exitoso", mensaje)

    def test_retiro_saldoInsuficiente_lanzaValueError(self):
        with self.assertRaises(ValueError):
            self.cuenta.retiro_cuenta(500)

    # ----------------------------
    # TRANSFERENCIA
    # ----------------------------
    def test_transferencia_aCuenta_transfiereCorrectamente(self):
        mensaje = self.cuenta.transferencia_cuenta(30, self.cuenta_destino)
        self.assertEqual(self.cuenta.saldo, 70.0)
        self.assertEqual(self.cuenta_destino.saldo, 80.0)
        self.assertIn("Transferencia exitosa", mensaje)

    def test_transferencia_aTexto_reduceSaldo(self):
        mensaje = self.cuenta.transferencia_cuenta(20, "Cuenta Externa")
        self.assertEqual(self.cuenta.saldo, 80.0)
        self.assertIn("Transferido a", mensaje)

    def test_transferencia_destinoInvalido_lanzaTypeError(self):
        with self.assertRaises(TypeError):
            self.cuenta.transferencia_cuenta(10, 12345)

    # ----------------------------
    # CONSULTA DE SALDO
    # ----------------------------
    def test_saldoCuenta_retornaSaldoCorrecto(self):
        self.assertEqual(self.cuenta.saldo_cuenta(), 100.0)


if __name__ == "__main__":
    unittest.main()
