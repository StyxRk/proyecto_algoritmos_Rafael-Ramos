import pip._vendor.requests as requests
from Equipos import *
from Estadios import *
from Partidos import *
from Producto import *
from Restaurante import *
from User import *
from Gestion_asistencia import *
from Gestion_entradas import *
from Gestion_restaurantes import *
from Gestion_ventas import * 
from Gestion_estadísticas import *
from random import *
import string

class Euro2024:
      def __init__(self):
            self.estadios = []
            self.ids_estadios = {}
            self.partidos = []
            self.ids_partidos = {}
            self.fechas_partidos = {}
            self.equipos = []
            self.ids_equipos = {}
            self.name_equipos = {}
            self.restaurantes = []
            self.ids_restaurantes = {}
            self.productos = []
            self.bebidas = []
            self.comidas = []
            self.estadio_actual = None
            self.user_logged = None
            self.users = []
            self.gestion_asistencias= Gestion_asistencia(self)
            self.gestion_entradas = Gestion_entradas(self)
            self.gestion_restaurantes = Gestion_restaurantes(self)
            self.gestion_ventas = Gestion_ventas(self)
            self.estadisticas = Gestion_estadisticas(self)
            self.total_pagar = 0

      def pedir_api(self):
            request_estadios = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json")
            estadios_data = request_estadios.json()

            request_equipos = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json")
            equipos_data = request_equipos.json()

            request_partidos = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json")
            partidos_data = request_partidos.json()

            if request_estadios.status_code == 200 and request_equipos.status_code == 200 and request_partidos.status_code == 200:
                  self.estadios = self.generar_objetos_estadio(estadios_data)
                  self.equipos = self.generar_objetos_equipo(equipos_data)
                  self.partidos = self.generar_objetos_partido(partidos_data)
                  print('Se generaron las listas de objetos de manera exitosa.')

            else:
                  print("La creacion de objetos no fue efectiva")


      def generar_objetos_estadio(self, estadios):
            lista_estadio = []

            for estadio in estadios:
                  id = estadio["id"]
                  name = estadio["name"]
                  city = estadio["city"]
                  capacity = estadio["capacity"]
                  restaurants = self.generar_objetos_restaurante(estadio["restaurants"])
                  regular_seats = self.generate_seats(capacity[0], estadio)
                  vip_seats = self.generate_seats(capacity[1], name)


                  self.ids_estadios[name] = id
                  nuevo_estadio = Estadio(id, name, city, capacity, restaurants,regular_seats, vip_seats)
                  lista_estadio.append(nuevo_estadio)
            
            return lista_estadio


      def generar_objetos_equipo(self, equipos):
            lista_equipos = []

            for equipo in equipos:
                  id = equipo["id"]
                  code = equipo["code"]
                  name = equipo["name"]
                  group = equipo["group"]            

                  nuevo_equipo = Equipo(id, code, name, group)
                  self.ids_equipos[name] = id
                  self.name_equipos[name] = code
                  lista_equipos.append(nuevo_equipo)

            return lista_equipos 



      def generar_objetos_partido(self, partidos):
            lista_partido = []

            for partido in partidos:
                  id = partido["id"]
                  number = partido["number"]
                  home = None
                  for equipo in self.equipos:
                        if partido["home"]["id"] == equipo.id :
                              home = equipo
                              break

                  away = None
                  for equipo in self.equipos:
                        if partido["away"]["id"] == equipo.id :
                              away = equipo
                              break

                  date = partido["date"]
                  group = partido["group"]
                  stadium_id = None
                  for estadio in self.estadios:
                        if partido["stadium_id"] == estadio.id:
                              stadium_id = estadio
                              break
                  encounter = f"{home.name} vs {away.name}"

                  nuevo_partido = Partido(id, number, home, away, date, group, stadium_id)
                  lista_partido.append(nuevo_partido)
                  self.ids_partidos[encounter] = id
                  self.fechas_partidos[encounter] = date

            return lista_partido



      def generar_objetos_restaurante(self, restaurantes):
            lista_restaurantes = []

            for restaurante in restaurantes:
                  name = restaurante["name"]
                  products = self.generar_objetos_productos(restaurante["products"])

                  nuevo_restaurante = Restaurante(name, products)
                  restaurant = nuevo_restaurante.show_restaurant
                  if nuevo_restaurante not in self.restaurantes:
                        self.restaurantes.append(restaurant)
                        
                  lista_restaurantes.append(nuevo_restaurante)
                  
            return lista_restaurantes

      def generar_objetos_productos(self, productos):
            lista_productos = []
            for producto in productos:
                  name = producto["name"]
                  quantity = producto["quantity"]
                  price = producto["price"]
                  adicional = producto["adicional"]
                  stock = producto["stock"]
                  if producto["adicional"] == "alcoholic" or producto["adicional"] == "non-alcoholic":
                        nuevo_producto = Bebida(name, quantity, price, adicional, stock)
                        if nuevo_producto not in self.bebidas:
                              self.bebidas.append(nuevo_producto)
                  elif producto["adicional"] == "plate" or producto["adicional"] == "plate":
                        nuevo_producto = Comida(name, quantity, price, adicional, stock)
                        if nuevo_producto not in self.comidas:
                              self.comidas.append(nuevo_producto)
                        lista_productos.append(nuevo_producto)

            return lista_productos


      def buscar_partidos_codigo (self):
            print(self.name_equipos)
            codigo = input("""Introduzca el codigo FIFA del pais que desea buscar 
                                       'Por ejemplo: Germany > GER'
                                       """).upper()

            for team in self.equipos:
                  if team.code == codigo:
                        partidos_equipo = []
                        seleccionado = team
                        nombre = team.name
                        for partido in self.partidos:
                              if partido.home == seleccionado or partido.away == seleccionado:
                                    encounter = f"{partido.home.name} vs {partido.away.name}"
                                    partidos_equipo.append(encounter)

                        print(f"La lista de partidos del equipo {nombre} de codigo {codigo} es {partidos_equipo}")

      def buscar_partidos_ID(self):
            print(self.ids_equipos)
            codigo = input("""Introduzca el id del pais que desea buscar 
                           """)
            for team in self.equipos:
                  if codigo == team.id:
                        partidos_equipo = []
                        seleccionado = team
                        nombre = team.name
                        for partido in self.partidos:
                              if partido.home == seleccionado or partido.away == seleccionado:
                                    encounter = f"{partido.home.name} vs {partido.away.name}"
                                    partidos_equipo.append(encounter)

                        print(f"La lista de partidos del equipo {nombre} de codigo {codigo} es {partidos_equipo}")
      
      def buscar_estadios_id(self):
            print(self.ids_estadios)
            codigo = input("""Introduzca el id del estadio que desea buscar
                           """)

            lista_partidos_estadio = []
            for partido in self.partidos:
                  if codigo == partido.stadium_id:
                        encounter = f"{partido.home} vs {partido.away}"
                        lista_partidos_estadio.append(encounter)

            for estadio in self.estadios:
                  if codigo == estadio.id:
                        nombre_estadio = estadio.name
                        break

            print(f"En el estadio {nombre_estadio}, los partidos a disputar son {lista_partidos_estadio}")


      def buscar_partidos_fecha(self):
            print(self.fechas_partidos)
            codigo = input("""Introduzca la fecha donde se celebraran los partidos de interes 
                           /'year-month-day'/
                           """)
            
            lista_partidos = []
            for partido in self.partidos:
                  if codigo == partido.date:
                        encounter = f"{partido.home} vs {partido.away}"
                        lista_partidos.append(encounter)

            print(f"""Los partidos a realizar en la fecha {codigo}, son los siguientes:
                  {lista_partidos}""")
            
      def cerrar_sesion(self):
            self.user_logged = None
            self.estadisticas.menu()
            self.total_pagar = 0
            print("Has cerrado tu sesion exitosamente")

      def iniciar_sesion(self):
            print("-------Creacion de usuario-------")
            nombre = input("Introduzca su primer nombre y primer apellido: ")
            cedula = input("Introduzca su cedula, que esta no exceda de ocho digitos:  ")
            while len(cedula) != 8:
                   cedula = input("Introduzca su cedula, que esta no difiera de ocho digitos:   ")
            edad = int(input("Introduzca la edad del usuario (Mayor a 7 años):   "))
            while not (edad > 6 and edad < 100):
                   edad = int(input("Introduzca la edad del usuario (Mayor a 7 años):   "))
            password = input("Introduzca su contrasena, que oscile entre 8 y 20 caracteres:    ")
            while not (len(password) > 7 and len(password) < 21):
                  password = input("Introduzca su contrasena, que oscile entre 8 y 20 caracteres:   ")
            nuevo_usuario = User(nombre, cedula, edad, password)
            self.user_logged = nuevo_usuario
            self.users.append(nuevo_usuario)
            print("Creacion de usuario efectiva")
            print(f"Bienvenido {nombre} a la Euro2024")
            print(f"""Tu informacion personal es: 
                  {nuevo_usuario}""")

      def show_matches(self):
            lista_partidos = []
            for partido in self.partidos:
                  cadena = f"""
                  id: {partido.id}
                  Encuentro: {partido.home} vs {partido.away}
                  Grupo: {partido.group}
                  Dia: {partido.day}
                  """
                  lista_partidos.append(cadena)
            print(cadena)

      def generate_seats(self, capacity, name):
            lista_asientos = {}
            cont = 0
            asientos_no_generados = capacity
            filas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            for letra in filas:
                  nuevos_asientos = {}
                  if asientos_no_generados != 0:
                        break
                  if cont > 20:
                        cont = 0
                        lista_asientos[f"Fila{letra}"] = nuevos_asientos
                        nuevos_asientos = {}
                  for num in range(21):
                        asiento = {}
                        codigo = self.generate_random_string()
                        asiento["estadio"] = name
                        asiento["codigo"] = codigo
                        asiento["disponibilidad"] = "no usado"
                        nuevos_asientos[f"{letra}.{num}"] = asiento
                        cont += 1
                        asientos_no_generados -= 1

            return lista_asientos
      
      def generate_random_string(self):
            n = 5

            res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=n))
            
            return res
 

      def menu(self):
            while True:
                  if self.user_logged != None:
                        print("----------Bienvenido usuario de la Eurocopa 2024----------")
                        opcion = input("""
                                       Seleccione que quiere hacer con este programa
                                    1. Buscar informacion de partidos/selecciones
                                    2. Gestionar venta de entradas
                                    3. Gestionar asistencia de partidos
                                    4. Gestionar compras en restaurantes
                                    5. Gestionar estadisticas
                                    6. Cerrar sesion
                                    7. salir
                                       
                                    """)
                        
                        if opcion == "1":
                              self.busqueda_por_filtros()

                        elif opcion == "2":
                              self.gestion_entradas.menu()
                        
                        elif opcion == "3":
                              self.gestion_asistencias.menu()

                        elif opcion == "4":
                              self.gestion_restaurantes.menu()

                        elif opcion == "5":
                              self.estadisticas.menu()

                        elif opcion == "6":
                              self.cerrar_sesion()
                        
                        elif opcion == "7":
                              print("Gracias por acceder a la euro2024!!!")
                              break

                        else:
                              print("Esta opcion no es valida, escriba un numero apto para el programa")

                  else:
                        print("-----Bienvenido a Euro2024-------")
                        opcion = input("""Que desea hacer en este momento?
                                    
                                          
                                    1. Iniciar sesion
                                    2. Salir
                                          
                                          
                                    """)
                        
                        if opcion == "1":
                              self.iniciar_sesion()
                              
                        
                        elif opcion == "2":
                              print("-------Gracias por usar Euro2024---------")

                        else:
                              print("Por favor, introduzca una opcion valida")


      
      def busqueda_por_filtros(self):
            while True:
                  print("------Bienvenido a la busqueda por filtros-------")
                  filtro = input("""
                              En base a que filtro desea hacer su busquedad?
                                 
                              1. Buscar partidos de un solo pais
                              2. Buscar todos los partidos de un estadio especifico
                              3. Buscar partidos de una fecha especifica
                              4. salir""")
                  
                  if filtro == "1":
                        opcion = input("""
                                       1. Filtrar por codigo
                                       2. Filtrar por id
                                       3. Salir
                                       
                                       
                                       """)
                        
                        if opcion == "1":
                              self.buscar_partidos_codigo()

                        elif opcion == "2":
                              self.buscar_partidos_ID()

                        elif opcion == "3":
                              continue

                  elif filtro == "2":
                        self.buscar_estadios_id()


                  elif filtro == "3":
                        self.buscar_partidos_fecha()

                  elif filtro == "4":
                        break



            

            

