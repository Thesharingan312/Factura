import datetime

class Articulo:
    def __init__(self, nombre, precio_unitario, cantidad):
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.cantidad = cantidad
        self.subtotal = self.precio_unitario * self.cantidad

    def __str__(self):
        return f"{self.nombre} x {self.cantidad} @ ${self.precio_unitario:.2f} = ${self.subtotal:.2f}"


class Factura:
    def __init__(self, cliente, fecha=None):
        self.cliente = cliente
        self.fecha = fecha if fecha is not None else datetime.datetime.now().strftime("%d/%m/%Y")
        self.articulos = []
        self.total = 0.0

    def agregar_articulo(self, articulo):
        self.articulos.append(articulo)
        self.total += articulo.subtotal

    def mostrar_factura(self):
        print("\n----- FACTURA -----")
        print(f"Cliente: {self.cliente}")
        print(f"Fecha: {self.fecha}")
        print("Productos:")
        for item in self.articulos:
            print(f"  - {item}")
        print(f"Total: ${self.total:.2f}")
        print("-------------------\n")


class SistemaFacturacion:
    def __init__(self):
        self.facturas = []
        self.total_general = 0.0

    def crear_factura(self):
        cliente = input("Nombre del cliente: ")
        fecha = input("Fecha (dd/mm/aaaa): ")
        factura = Factura(cliente, fecha)

        while True:
            producto = input("Nombre del producto (o escribe 'fin' para terminar): ")
            if producto.lower() == 'fin':
                break
            try:
                precio = float(input(f"Precio de '{producto}': $"))
                cantidad = int(input(f"Cantidad de '{producto}': "))
                articulo = Articulo(producto, precio, cantidad)
                factura.agregar_articulo(articulo)
            except ValueError:
                print("⚠️ Error: ingresa valores válidos para precio y cantidad.")

        factura.mostrar_factura()
        self.facturas.append(factura)
        self.total_general += factura.total

    def mostrar_resumen(self):
        print("\n======= RESUMEN DE FACTURAS =======")
        for f in self.facturas:
            print(f"{f.fecha} - {f.cliente} - Total: ${f.total:.2f}")
        print(f"TOTAL GENERAL FACTURADO: ${self.total_general:.2f}")
        print("===================================")

    def ejecutar(self):
        print("======= BIENVENIDO AL SISTEMA DE FACTURACIÓN =======")
        while True:
            self.crear_factura()
            otra = input("¿Deseas crear otra factura? (s/n): ")
            if otra.lower() != 's':
                break
        self.mostrar_resumen()


# Punto de entrada del programa
if __name__ == "__main__":
    sistema = SistemaFacturacion()
    sistema.ejecutar()
