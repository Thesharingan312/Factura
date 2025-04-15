class Articulo:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        total = self.precio * self.cantidad
        return f"{self.nombre} - {self.cantidad} x ${self.precio:.2f} = ${total:.2f}"


class Factura:
    def __init__(self, cliente, fecha):
        self.cliente = cliente
        self.fecha = fecha
        self.articulos = []
        self.total = 0.0

    def agregar_articulo(self, articulo):
        self.articulos.append(articulo)
        self.total += articulo.precio * articulo.cantidad

    def limpiar_factura(self):
        self.articulos.clear()
        self.total = 0.0

    def __str__(self):
        cabecera = f"Factura para {self.cliente} - Fecha: {self.fecha}\n"
        detalle = "\n".join(str(a) for a in self.articulos)
        return f"{cabecera}\n{detalle}\n\nTOTAL: ${self.total:.2f}"


class SistemaFacturacion:
    def __init__(self):
        self.facturas = []
        self.total_general = 0.0

    def generar_factura(self, cliente, fecha, lista_articulos):
        factura = Factura(cliente, fecha)
        for art in lista_articulos:
            factura.agregar_articulo(art)
        self.facturas.append(factura)
        self.total_general += factura.total
        return factura

    def limpiar_facturas(self):
        self.facturas.clear()
        self.total_general = 0.0
