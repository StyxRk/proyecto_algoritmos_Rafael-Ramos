class User:
    def __init__(self, name, cedula, age, password, entradas_generales = [], entradas_vip = [], gastos = 0):
        self.name = name
        self.cedula = cedula
        self.age = age
        self.password = password
        self.entradas_generales = entradas_generales
        self.entradas_vip = entradas_vip
        self.gastos = gastos
        

    def __str__(self):
        return f"""
        Nombre: {self.name}
        Edad: {self.age}
        Cedula: {self.cedula}
        Contraseña: {self.password}
        Entradas generales: {self.entradas_generales}
        Entradas VIP: {self.entradas_vip}
        gastos: {self.gastos}
        """
    
    def show_entradas(self):
        return f"""
        Entradas generales: {self.entradas_generales}
        Entradas Vip: {self.entradas_vip}
        """