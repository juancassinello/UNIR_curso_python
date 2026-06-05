
class Producto:

    def __init__(self, nombre, precio, cantidad):

        # validación:
        # --- no debe estar vacío.
        # --- debe ser un string.
        if type(nombre) is str and nombre.strip():
            self.nombre = nombre

            # validación:
            # --- debe ser un float.
            # --- debe ser mayor o igual que cero.
            if type(precio) is float and precio >= 0:
                self.precio = precio

                # validación:
                # --- debe ser un int
                # --- sea mayor o igual a cero.
                if type(cantidad) is int and cantidad >= 0:
                    self.cantidad = cantidad

                else:
                    print("La cantidad debe ser un número entero mayor o igual a cero")
            else:
                print("El precio debe ser un valor decimal, y mayor o igual a cero")
        else:
            print("El nombre del producto debe ser texto y no puede estar vacío")

    def actualizar_precio(self, nuevo_precio):
        
        # validación:
        # --- debe ser un float.
        # --- debe ser mayor o igual que cero.
        if type(nuevo_precio) is float and nuevo_precio >= 0:
            self.precio = nuevo_precio

        else:
            print("El nuevo precio debe ser un valor decimal, y mayor o igual a cero")

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

    def __init__(self):
        self.lista_productos = []

    def agregar_producto(self, producto):

        if type(producto) is Producto:
             self.lista_productos.append(producto)
             print("Producto agregado correctamente")

        else:
            print("El parámetro recibido para agregar un producto al inventario no es del tipo correcto.")

    def buscar_producto(self, nombre):

        if type(nombre) is str and nombre.strip():
            for l in self.lista_productos:
                if l.nombre.lower() == nombre.lower():
                    return l
            
            # Si no hemos encontrado el nombre, devolvemos un None.
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

    def menu_principal(self):

        continuar = True

        while continuar:
            try:

                print("MENÚ")
                print("1. Agregar producto")
                print("2. Buscar producto")
                print("3. Listar productos")
                print("4. Calcular valor total del inventario")
                print("5. Salir")

                opcion = int(input("Ingrese el número de opción que desee: "))

                match opcion:
                    case 1:
                        producto_nombre = str(input("Introduzca el nombre del producto que desee: "))
                        
                        if producto_nombre.strip():
                            producto_precio = float(input("Introduzca el precio: "))
                            producto_cantidad = int(input("Introduzca la cantidad del producto: "))
                            
                            producto = Producto(producto_nombre, producto_precio, producto_cantidad)
                            inventario.agregar_producto(producto)
                        
                        else:
                            print("El nombre del producto no puede estar vacío")

                    case 2:
                        producto_nombre = input("Introduzca el nombre del producto a buscar: ")
                        if inventario.buscar_producto(producto_nombre) != None:
                            print("Producto encontrado en el inventario")
                        else:
                            print("Producto no encontrado en el inventario")
                    
                    case 3:
                        self.listar_productos()
                    
                    case 4:
                        print(f"El valor total del inventario es de {self.calcular_valor_inventario()} euros")
                    
                    case 5:
                        continuar = False

            except ValueError:
                print("Valor incorrecto. Vuelva a comenzar hasta hacerlo bien")


if __name__ == "__main__":
    inventario = Inventario()
    inventario.menu_principal()