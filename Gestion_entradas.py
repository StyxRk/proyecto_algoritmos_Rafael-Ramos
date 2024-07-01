import itertools as iter

class Gestion_entradas:
    def __init__(self, euro2024):
        self.euro2024 = euro2024


    def menu(self):
        print("-------Bienvenido a la gestion de entradas!!!!---------")
        while True:
            opcion = input("""Seleccione que desea hacer con este programa
                        1. Ver partidos
                        2. Comprar entradas
                        3. Salir""")
            
            if opcion == "1":
                print("-------Informacion de partidos--------")
                self.euro2024.show_matches()

            if opcion == "2":
                self.comprar_entrada(self.euro2024)

            if opcion == "3":
                break


    def comprar_entrada(self):
        self.euro2024.show_matches()

        id_partido = input("Introduzca el id del partido que desee consultar su informacion")

        for partido in self.euro2024.partidos:
            if id_partido == partido.id:
                id_estadio = partido.stadium_id
                for estadio in self.euro2024.estadios:
                    if id_estadio == estadio.id:
                        while True:
                            opcion = input("""
                                       Que asientos desea adquirir?
                                       1. Regulares
                                       2. VIP
                                       3. Salir
                                        
                                        """)
                            
                            if opcion == "1":
                                estadio.show_regular_seats(estadio.regular_seats, "regular")
                                adquiridos = self.escoger_asiento(estadio.regular_seats)
                                estadio.buyed_tickets += adquiridos

                            if opcion == "2":
                                estadio.show_vip_seats(estadio.vip_seats)
                                adquiridos = self.escoger_asiento(estadio.vip_seats, "vip")
                                estadio.buyed_tickets += adquiridos

                            if opcion == "3":
                                break
                        break
    
    def escoger_asiento(self, seats, entrada):
        while True:
            opcion = input("Desea salir? (si/no) ")

            if opcion == "no":
                print("""Escriba el codigo del asiento que desee adquirir:
                """)
                total = 0
                adquiridos = 0
                vip_adquiridos = 0
                regular_adquiridos = 0
                asiento = input("")
                found = ''
                for row in seats:
                    for seat in row:
                        if asiento == seat["codigo"] and seat["disponibilidad"] == "Disponible":
                            found == True
                        else:
                            print("Este asiento no esta disponible")

                        
                if found != True:
                    print("Asiento no encontrado, vuelva a buscar")

                else:
                    answer = input("""Desea adquirir este asiento?
                                (si/no)""")
                    if answer == "si" and entrada == "regular":
                        print("""Perfecto asiento adquirido!!!""")
                        for row in seats:
                            for seat in row:
                                if asiento == seat["codigo"]:
                                    self.euro2024.user_logged.entradas_generales.append(seat)
                                    seat["disponibilidad"] = "No disponible"
                                    seat["dueño"] = self.euro2024.user_logged.name
                                    regular_adquiridos += 1
                                    adquiridos+=1
                                    total += 35
                        
                    if answer == "si" and entrada == "vip":
                        print("""Perfecto asiento adquirido!!!""")
                        for row in seats:
                            for seat in row:
                                if asiento == seat["codigo"]:
                                    self.euro2024.user_logged.entradas_vip.append(seat)
                                    seat["disponibilidad"] = "No disponible"
                                    seat["dueño"] = self.euro2024.user_logged.name
                                    vip_adquiridos += 1
                                    adquiridos+=1
                                    total += 75


                    elif answer == "no":
                        print("Escoja otro asiento de su gusto ")
                        break

            elif opcion == "si":
                    self.revisar_gastos(total, regular_adquiridos, vip_adquiridos)
                    return adquiridos


    def revisar_gastos(self, total, regular_adquiridos, vip_adquiridos):
        print(f"""Usted ha adquirido un total de asientos 
              regulares: {regular_adquiridos}
              vip: {vip_adquiridos}""")
        
        print(f"""Su total a pagar por asientos es de {total}""")

        numero_vampiro = numero_vampiro(self.euro2024.user_logged.cedula)
        if numero_vampiro == 0.50:
            print("Enhorabuena, se le ha aplicado un descuento del 50 por ciento a sus entradas!!!")
        
        precio_cambiado = total*numero_vampiro*1.16
        self.euro2024.user_logged.gastos += precio_cambiado

        print(f"En total, ha de pagar {precio_cambiado}")
        print("Gracias por adquirir sus entradas!!!")

    def numero_vampiro(self, cedula):
        aux = str(cedula)
        if len(aux) % 2 != 0:
            return False
        permutations = iter.permutations(aux, len(aux))
        for permutation in permutations:
            first_half = permutation[:len(aux)//2]
            second_half = permutation[len(aux)//2:]
            first_half = "".join(first_half)
            second_half = "".join(second_half)

            if first_half[-1] == "0" and second_half[-1] == 0:
                continue

            if int(first_half) * int(second_half) == int(aux):
                return 0.50
        return 1