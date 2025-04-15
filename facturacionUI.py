
        # self.root.iconbitmap("icono.ico")
import tkinter as tk
from tkinter import ttk, messagebox
import datetime
from facturacion import SistemaFacturacion, Articulo, Factura

class FacturacionUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Facturación POS")
        self.root.geometry("700x600")

        self.sistema = SistemaFacturacion()
        self.factura_actual = None

        self._construir_interfaz()

        # Activar tema automático al iniciar si se selecciona
        if self.tema.get() == "Automático":
            self.cambiar_tema()

    def _construir_interfaz(self):
        estilo = ttk.Style()
        estilo.configure("TFrame", background="#f0f0f0")
        estilo.configure("TLabel", background="#f0f0f0", font=("Segoe UI", 10))
        estilo.configure("TButton", font=("Segoe UI", 10, "bold"))

        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self._crear_encabezado()
        self._crear_linea_articulos()
        self._crear_factura()
        self._crear_controles_finales()

    def _crear_encabezado(self):
        frame_encabezado = ttk.LabelFrame(self.frame, text="Datos del Cliente")
        frame_encabezado.pack(fill=tk.X, pady=5)

        ttk.Label(frame_encabezado, text="Cliente:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.cliente_entry = ttk.Entry(frame_encabezado, width=30)
        self.cliente_entry.grid(row=0, column=1, padx=5)

        ttk.Label(frame_encabezado, text="Fecha (dd/mm/aaaa):").grid(row=0, column=2, padx=5)
        self.fecha_entry = ttk.Entry(frame_encabezado, width=15)
        self.fecha_entry.grid(row=0, column=3, padx=5)

    def _crear_linea_articulos(self):
        frame_articulo = ttk.LabelFrame(self.frame, text="Agregar Producto")
        frame_articulo.pack(fill=tk.X, pady=5)

        ttk.Label(frame_articulo, text="Producto:").grid(row=0, column=0, padx=5, pady=5)
        self.producto_entry = ttk.Entry(frame_articulo, width=20)
        self.producto_entry.grid(row=0, column=1, padx=5)

        ttk.Label(frame_articulo, text="Precio:").grid(row=0, column=2, padx=5)
        self.precio_entry = ttk.Entry(frame_articulo, width=10)
        self.precio_entry.grid(row=0, column=3, padx=5)

        ttk.Label(frame_articulo, text="Cantidad:").grid(row=0, column=4, padx=5)
        self.cantidad_entry = ttk.Entry(frame_articulo, width=10)
        self.cantidad_entry.grid(row=0, column=5, padx=5)

        self.btn_agregar = ttk.Button(frame_articulo, text="Agregar", command=self.agregar_producto)
        self.btn_agregar.grid(row=0, column=6, padx=5)

    def _crear_factura(self):
        frame_factura = ttk.LabelFrame(self.frame, text="Factura Actual")
        frame_factura.pack(fill=tk.BOTH, expand=True, pady=5)

        self.lista_factura = tk.Listbox(frame_factura, height=10, font=("Consolas", 10))
        self.lista_factura.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.total_var = tk.StringVar(value="Total: $0.00")
        self.lbl_total = ttk.Label(frame_factura, textvariable=self.total_var, font=("Segoe UI", 12, "bold"))
        self.lbl_total.pack(pady=5)

    def _crear_controles_finales(self):
        frame_controles = ttk.Frame(self.frame)
        frame_controles.pack(fill=tk.X, pady=10)

        self.btn_guardar = ttk.Button(frame_controles, text="Guardar Factura", command=self.guardar_factura)
        self.btn_guardar.pack(side=tk.LEFT, padx=5)

        self.btn_limpiar = ttk.Button(frame_controles, text="Limpiar Todo", command=self.limpiar_formulario)
        self.btn_limpiar.pack(side=tk.LEFT, padx=5)

        ttk.Label(frame_controles, text="Tema: ").pack(side=tk.LEFT, padx=5)
        self.tema = ttk.Combobox(frame_controles, values=["Claro", "Oscuro", "Alto Contraste", "Automático"], width=18)
        self.tema.pack(side=tk.LEFT, padx=5)
        self.tema.bind("<<ComboboxSelected>>", self.cambiar_tema)
        self.tema.set("Claro")

    def agregar_producto(self):
        try:
            nombre = self.producto_entry.get()
            precio = float(self.precio_entry.get())
            cantidad = int(self.cantidad_entry.get())
            articulo = Articulo(nombre, precio, cantidad)

            if not self.factura_actual:
                cliente = self.cliente_entry.get()
                fecha = self.fecha_entry.get()
                self.factura_actual = Factura(cliente, fecha)

            self.factura_actual.agregar_articulo(articulo)
            self.lista_factura.insert(tk.END, str(articulo))
            self.total_var.set(f"Total: ${self.factura_actual.total:.2f}")

        except ValueError:
            messagebox.showerror("Error", "⚠️ Ingresa datos válidos para el producto.")

    def guardar_factura(self):
        if self.factura_actual:
            self.sistema.facturas.append(self.factura_actual)
            self.sistema.total_general += self.factura_actual.total
            messagebox.showinfo("Factura Guardada", "✅ La factura se guardó exitosamente.")
            self.limpiar_formulario()

    def limpiar_formulario(self):
        self.cliente_entry.delete(0, tk.END)
        self.fecha_entry.delete(0, tk.END)
        self.producto_entry.delete(0, tk.END)
        self.precio_entry.delete(0, tk.END)
        self.cantidad_entry.delete(0, tk.END)
        self.lista_factura.delete(0, tk.END)
        self.total_var.set("Total: $0.00")
        self.factura_actual = None

    def cambiar_tema(self, evento=None):
        seleccion = self.tema.get()

        # Si el modo es Automático, decide según la hora
        if seleccion == "Automático":
            hora_actual = datetime.datetime.now().hour
            if 6 <= hora_actual < 18:
                seleccion = "Claro"
            else:
                seleccion = "Oscuro"

        colores = {
            "Claro": {
                "bg": "#f0f0f0", "fg": "#000000",
                "entry_bg": "white", "listbox_bg": "white", "listbox_fg": "black"
            },
            "Oscuro": {
                "bg": "#2e2e2e", "fg": "#ffffff",
                "entry_bg": "#3b3b3b", "listbox_bg": "#1e1e1e", "listbox_fg": "#ffffff"
            },
            "Alto Contraste": {
                "bg": "#000000", "fg": "#ffff00",
                "entry_bg": "#000000", "listbox_bg": "#000000", "listbox_fg": "#ffff00"
            }
        }

        if seleccion in colores:
            paleta = colores[seleccion]
            self.root.configure(bg=paleta["bg"])
            self.frame.configure(style="Custom.TFrame")

            estilo = ttk.Style()
            estilo.configure("Custom.TFrame", background=paleta["bg"])
            estilo.configure("TLabel", background=paleta["bg"], foreground=paleta["fg"])
            estilo.configure("TLabelFrame", background=paleta["bg"], foreground=paleta["fg"])
            estilo.configure("TButton", background=paleta["bg"], foreground=paleta["fg"])
            estilo.configure("TEntry", fieldbackground=paleta["entry_bg"], foreground=paleta["fg"])

            for entry in [self.cliente_entry, self.fecha_entry, self.producto_entry, self.precio_entry, self.cantidad_entry]:
                entry.configure(background=paleta["entry_bg"], foreground=paleta["fg"])

            self.lista_factura.configure(bg=paleta["listbox_bg"], fg=paleta["listbox_fg"])


if __name__ == "__main__":
    root = tk.Tk()
    app = FacturacionUI(root)
    root.mainloop()
