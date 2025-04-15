class Articulo:
    """
    Representa un artículo que puede ser añadido a una factura.

    Atributos:
        nombre (str): El nombre del artículo.
        precio (float): El precio unitario del artículo.
        cantidad (int): La cantidad de unidades del artículo.
    """

    def __init__(self, nombre, precio, cantidad):
        """
        Inicializa un nuevo artículo.

        Args:
            nombre (str): Nombre del artículo.
            precio (float): Precio por unidad.
            cantidad (int): Número de unidades.
        """
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        """
        Representación en texto del artículo para mostrar en listas o impresión.

        Returns:
            str: Detalle del artículo con cantidad, nombre y precio total.
        """
        return f"{self.cantidad} x {self.nombre} @ ${self.precio:.2f} = ${self.precio * self.cantidad:.2f}"


class Factura:
    """
    Representa una factura que contiene múltiples artículos.

    Atributos:
        cliente (str): Nombre del cliente.
        fecha (str): Fecha de emisión de la factura.
        articulos (list): Lista de objetos Articulo en la factura.
        total (float): Suma total de los precios de todos los artículos.
    """

    def __init__(self, cliente, fecha):
        """
        Crea una nueva factura.

        Args:
            cliente (str): Nombre del cliente.
            fecha (str): Fecha de la factura.
        """
        self.cliente = cliente
        self.fecha = fecha
        self.articulos = []
        self.total = 0.0

    def agregar_articulo(self, articulo):
        """
        Agrega un artículo a la factura.

        Args:
            articulo (Articulo): Objeto Articulo a añadir.
        """
        self.articulos.append(articulo)
        self.total += articulo.precio * articulo.cantidad

    def __str__(self):
        """
        Representación textual de la factura completa.

        Returns:
            str: Texto con el detalle de la factura, incluyendo todos los artículos y total.
        """
        detalle = "\n".join(str(a) for a in self.articulos)
        return f"Factura para {self.cliente} - {self.fecha}\n{detalle}\nTotal: ${self.total:.2f}"


class SistemaFacturacion:
    """
    Sistema de facturación general que permite almacenar múltiples facturas.

    Atributos:
        facturas (list): Lista de objetos Factura creados.
        total_general (float): Total acumulado de todas las facturas registradas.
    """

    def __init__(self):
        """
        Inicializa el sistema de facturación.
        """
        self.facturas = []
        self.total_general = 0.0

    def agregar_factura(self, factura):
        """
        Agrega una nueva factura al sistema.

        Args:
            factura (Factura): Objeto Factura que se agregará.
        """
        self.facturas.append(factura)
        self.total_general += factura.total

    def obtener_total_general(self):
        """
        Obtiene el total acumulado de todas las facturas.

        Returns:
            float: Suma total de todas las facturas registradas.
        """
        return self.total_general
