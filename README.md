# Sistema de Facturación en Python

¡Hola! Bienvenido al repositorio del Sistema de Facturación en Python. Este proyecto es una aplicación sencilla que te permite crear facturas, agregar productos y visualizar un resumen de ventas. Además, cuenta con una interfaz gráfica desarrollada con Tkinter para hacerlo más amigable.

## ¿Qué hace este proyecto?

- **Backend (facturacion.py):**  
  Implementa las clases `Articulo`, `Factura` y `SistemaFacturacion` para gestionar facturas y calcular totales.  
- **Interfaz Gráfica (facturacionUI.py):**  
  Usa Tkinter para que puedas ingresar los datos del cliente y los artículos, ver la lista de productos y mostrar la factura final en una ventana.

## ¿Cómo empezar?

### Requisitos

- Python 3.6 o superior.
- Módulos: Tkinter (viene con Python), y los demás módulos son parte de la librería estándar.

### Instalación

1. Clona el repositorio:
   ```bash
   git clone https://tu-repo-url.git
¿Cómo se probó?
Se incluyó un archivo de tests unitarios (test_facturacion.py) usando el módulo unittest. Puedes ejecutarlos con:

bash
Copiar
python -m unittest test_facturacion.py
