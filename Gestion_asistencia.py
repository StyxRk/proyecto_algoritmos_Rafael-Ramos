class Gestion_asistencia:
    def __init__(self, euro2024):
        self.euro2024 = euro2024

    def menu(self):
        while True:
            self.euro2024.user_logged.show_entradas()

            print("-----Bienvenido a gestion de asistencias--------")

            opcion = input("""Indique, que opcion tomara?
                           1. Asistir a un partido
                           2. Salir""")
            
            if opcion == "1":
                codigo = input("Ingrese el codigo de asiento de su gusto")

            if opcion == "2":
                break

    