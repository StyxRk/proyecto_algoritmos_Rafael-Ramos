class Estadio:
    def __init__(self, id = "", name = "", city = "", capacity = 0, restaurants = [], regular_seats = {}, vip_seats = {}, buyed_tickets = 0):
        self.id = id
        self.name = name
        self.city = city
        self.capacity = capacity
        self.restaurants = restaurants
        self.regular_seats = regular_seats
        self.vip_seats = vip_seats
        self.buyed_tickets = buyed_tickets

    def show_attr(self):
        return f"""
        Id: {self.id}
        Nombre: {self.name}
        Ciudad: {self.city}
        Capacidad: {self.capacity}
        Restaurantes: {self.restaurants}
        Entradas compradas: {self.buyed_tickets}

        """
    
    def show_regular_seats(self, seats):
        regular_seats = []
        for i, row in enumerate(seats):
            for j, seat in enumerate(row):
                new_seat = f"{j+1}.{seat}"
                regular_seats.append(new_seat)

        return regular_seats
    
    def show_vip_seats(self, seats):
        VIP_seats = []
        for i, row in enumerate(seats):
            for j, seat in enumerate(row):
                new_seat = f"{j+1}.{seat}"
                VIP_seats.append(new_seat)

        return VIP_seats