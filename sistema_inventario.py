
class Producto:

    def __init__(self, nombre, precio, cantidad):

        # validación: el nombre no esté vacío.
        self.nombre = nombre
        
        # validación: precio sea mayor o igual que cero.
        self.precio = precio

        # validación: la cantidad sea mayor o igual a cero.
        self.cantidad = cantidad

        