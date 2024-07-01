class Equipo:
    def __init__(self, id = "", code = "", name = "", group = ""):
        self.id = id
        self.code = code
        self.name = name
        self.group = group

    def show_attr(self):
        return f"""
        id: {self.id}
        Codigo: {self.code}
        Nombre: {self.name}
        Grupo: {self.group}
        """
    
    