class Partido:
    def __init__(self, id = "", number = "", home = "", away = "", date = "", group = "", stadium_id = "", buyed_tickets = 0):
            self.id = id
            self.number = number
            self.home = home
            self.away = away
            self.date = date
            self.group = group
            self.stadium_id = stadium_id
            self.buyed_tickets = buyed_tickets

    def show_attr(self):
        return f""" ---------Partido---------
    Id: {self.id}
    Numero: {self.number}
    Local: {self.home}
    Visitante: {self.away}
    Fecha: {self.date}
    Grupo: {self.group}
    Id_Estadio: {self.stadium_id}
    """