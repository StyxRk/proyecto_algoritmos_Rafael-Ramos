class Producto:
    def __init__(self, name = "", quantity = 0, price = 0, stock = 0):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.stock = stock

class Bebida(Producto):

    def __init__(self, name, quantity, price, adicional, stock, tipo = "bebida"):
        super().__init__(name, quantity, price, stock)
        self.adicional = adicional
        self.tipo = tipo

    def show_product(self):
        return f"""
    Nombre: {self.name}
    Tipo: {self.tipo}
    Cantidad: {self.quantity}
    Precio: {self.price}
    Adicional: {self.adicional}
    Reserva: {self.stock}
    Tipo: {self.tipo}

    """

class Comida (Producto):
    def __init__(self, name, quantity, price, adicional, stock, tipo = "Comida"):
        super().__init__(name, quantity, price, stock)
        self.adicional = adicional
        self.tipo = tipo

    def show__product(self):
        return f"""
    Nombre: {self.name}
    Tipo: {self.tipo}
    Cantidad: {self.quantity}
    Precio: {self.price}
    Adicional: {self.aditional}
    Reserva: {self.stock}
    Tipo: {self.tipo}

    """