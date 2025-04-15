import unittest
from io import StringIO
import sys

# Importamos las clases desde el archivo principal
from facturacion import Articulo, Factura, SistemaFacturacion

class TestSistemaFacturacion(unittest.TestCase):

    def test_creacion_articulo(self):
        art = Articulo("Café", 3.50, 2)
        self.assertEqual(art.nombre, "Café")
        self.assertEqual(art.precio_unitario, 3.50)
        self.assertEqual(art.cantidad, 2)
        self.assertEqual(art.subtotal, 7.00)

    def test_agregar_articulo_a_factura(self):
        factura = Factura("Juan", "14/04/2025")
        art1 = Articulo("Pan", 1.00, 3)
        art2 = Articulo("Leche", 1.50, 2)
        factura.agregar_articulo(art1)
        factura.agregar_articulo(art2)
        self.assertEqual(len(factura.articulos), 2)
        self.assertEqual(factura.total, 6.0)

    def test_mostrar_factura_salida(self):
        factura = Factura("Ana", "14/04/2025")
        factura.agregar_articulo(Articulo("Azúcar", 2.0, 1))
        
        captured_output = StringIO()
        sys.stdout = captured_output
        factura.mostrar_factura()
        sys.stdout = sys.__stdout__

        salida = captured_output.getvalue()
        self.assertIn("Cliente: Ana", salida)
        self.assertIn("Azúcar", salida)
        self.assertIn("Total: $2.00", salida)

if __name__ == '__main__':
    unittest.main()
