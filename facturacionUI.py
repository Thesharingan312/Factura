import tkinter as tk
from tkinter import messagebox
from facturacion import Articulo, Factura

class FacturacionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Facturación")

        # Factura y datos
        self.factura = None

        # Widgets de cliente
        tk.Label(root, text="Nombre del Cliente:").grid(row=0, column=0)
        self.entry_cliente = tk.Entry(root)
        self.entry_cliente.grid(row=0, column=1)

        # Artículo - nombre, precio, cantidad
        tk.Label(root, text="Producto:").grid(row=1, column=0)
        self.entry_producto = tk.Entry(root)
        self.entry_producto.grid(row=1, column=1)

        tk.Label(root, text="Precio:").grid(row=2, column=0)
        self.entry_precio = tk.Entry(root)
        self.entry_precio.grid(row=2, column=1)

        tk.Label(root, text="Cantidad:").grid(row=3, column=0)
        self.entry_cantidad = tk.Entry(root)
        self.entry_cantidad.grid(row=3, column=1)

        # Botón agregar artículo
        self.boton_agregar = tk.Button(root, text="Agregar artículo", command=self.agregar_articulo)
        self.boton_agregar.grid(row=4, column=0, columnspan=2, pady=5)

        # Texto de factura
        self.text_factura = tk.Text(root, width=60, height=15)
        self.text_factura.grid(row=5, column=0, columnspan=2, pady=10)

        # Botón mostrar factura final
        self.boton_mostrar = tk.Button(root, text="Mostrar Factura", command=self.mostrar_factura)
        self.boton_mostrar.grid(row=6, column=0, columnspan=2, pady=5)

    def agregar_articulo(self):
        nombre = self.entry_producto.get()
        try:
            precio = float(self.entry_precio.get())
            cantidad = int(self.entry_cantidad.get())
        except ValueError:
            messagebox.showerror("Error", "Precio y cantidad deben ser numéricos")
            return

        if not self.factura:
            cliente = self.entry_cliente.get()
            if not cliente:
                messagebox.showerror("Error", "Debes ingresar el nombre del cliente")
                return
            self.factura = Factura(cliente)

        nuevo_articulo = Articulo(nombre, precio, cantidad)
        self.factura.agregar_articulo(nuevo_articulo)

        self.text_factura.insert(tk.END, f"{cantidad} x {nombre} (${precio:.2f} c/u)\n")
        self.entry_producto.delete(0, tk.END)
        self.entry_precio.delete(0, tk.END)
        self.entry_cantidad.delete(0, tk.END)

    def mostrar_factura(self):
        if not self.factura or not self.factura.articulos:
            messagebox.showwarning("Advertencia", "No hay artículos en la factura")
            return

        self.text_factura.insert(tk.END, "\n--- FACTURA FINAL ---\n")
        self.text_factura.insert(tk.END, f"Cliente: {self.factura.nombre_cliente}\n")
        self.text_factura.insert(tk.END, f"Fecha: {self.factura.fecha}\n")
        self.text_factura.insert(tk.END, f"Total: ${self.factura.total:.2f}\n")

# Ejecución de la app
if __name__ == "__main__":
    root = tk.Tk()
    app = FacturacionApp(root)
    root.mainloop()
