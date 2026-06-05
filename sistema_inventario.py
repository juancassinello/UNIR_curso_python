
class Producto:

    def __init__(self, nombre, precio, cantidad):

        # validación:
        # --- no debe estar vacío.
        # --- debe ser un string.
        if type(nombre) is str and nombre.strip():
            self.nombre = nombre

            # validación:
            # --- debe ser un float o un int.
            # --- debe ser mayor o igual que cero.
            if (type(precio) is float or type(precio) is int) and precio >= 0:
                self.precio = precio

                # validación:
                # --- debe ser un int
                # --- sea mayor o igual a cero.
                if type(cantidad) is int and cantidad >= 0:
                    self.cantidad = cantidad

                else:
                    print("La cantidad debe ser un número entero mayor o igual a cero")
            else:
                print("El precio debe ser un entero o decimal, y mayor o igual a cero")
        else:
            print("El nombre del producto debe ser texto y no puede estar vacío")

    def actualizar_precio(self, nuevo_precio):
        
        # validación:
        # --- debe ser un float o un int.
        # --- debe ser mayor o igual que cero.
        if (type(nuevo_precio) is float or type(nuevo_precio) is int) and nuevo_precio >= 0:
            self.precio = nuevo_precio

        else:
            print("El nuevo precio debe ser un entero o decimal, y mayor o igual a cero")

    def actualizar_cantidad(self, nueva_cantidad):
        # validación:
        # --- debe ser un int
        # --- sea mayor o igual a cero.        
        if type(nueva_cantidad) is int and nueva_cantidad >= 0:
            self.cantidad = nueva_cantidad
        
        else:
            print("La nueva cantidad debe ser un número entero mayor o igual a cero")

    def calcular_valor_total(self):
        return self.precio * self.cantidad

    def __str__ (self):
        return f"El producto {self.nombre} tiene un precio de {self.precio} euros y una cantidad de {self.cantidad} unidades"

class Inventario:

    lista_productos = []

    def agregar_producto(self, producto):

        if type(producto) is Producto:
             self.lista_productos.append(producto)
        
        else:
            print("El parámetro recibido para agregar un producto al inventario no es del tipo correcto.")

    def buscar_producto(self, nombre):

        if type(nombre) is str and nombre.strip():
            for l in self.lista_productos:
                if l.nombre.lower() == nombre.lower():
                    return l
                else:
                    return None
        else:
            print("El nombre del producto debe ser texto y no puede estar vacío")

    def calcular_valor_inventario(self):
        
        valor_total = 0

        for l in self.lista_productos:
            valor_total += l.calcular_valor_total()

        return valor_total

    def listar_productos(self):
        for l in self.lista_productos:
            print(l)

    def menu_principal():
        '''
            MENÚ
            1. Agregar producto
            2. Buscar producto
            3. Listar productos
            4. Calcular valor total del inventario
            5. Salir
        '''

if __name__ == "__main__":
    # instancia un objeto de la clase Inventario y llama a la función menu_principal() para iniciar la aplicación

    inventario = Inventario()    
    pera = Producto("Pera", 7.9, 10)
    manzana = Producto("Manzana", 3.5, 100)

    inventario.agregar_producto(pera)
    inventario.agregar_producto(manzana)

    print(inventario.calcular_valor_inventario())