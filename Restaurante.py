class Restaurante:
    def __init__(self, name, products):
        self.name = name
        self.products = products
        

    def show_restaurant(self):
        return f"""--------Restaurante----------
        Nombre: {self.name}
        Productos: {self.products}"""
    
    
   