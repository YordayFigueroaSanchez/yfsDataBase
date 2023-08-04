class Jugador:
    def __init__(self, nombre, numero):
        self.nombre = nombre
        self.numero = numero
        self.estadisticas = EstadisticasJugador()

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

class EstadisticasJugador:
    def __init__(self):
        self.puntos = 0
        self.rebotes = 0
        self.asistencias = 0

class Juego:
    def __init__(self, equipo_local, equipo_visitante):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante

# Crear instancias de equipos
equipo_local = Equipo("Equipo Local")
equipo_visitante = Equipo("Equipo Visitante")

# Crear instancias de jugadores y agregarlos a los equipos
jugador1 = Jugador("Jugador 1", 1)
jugador2 = Jugador("Jugador 2", 2)
jugador3 = Jugador("Jugador 3", 3)

equipo_local.agregar_jugador(jugador1)
equipo_local.agregar_jugador(jugador2)
equipo_visitante.agregar_jugador(jugador3)

# Acceder a los jugadores de un equipo
for jugador in equipo_local.jugadores:
    print(jugador.nombre)    # Jugador 1, Jugador 2

# Acceder a las estadísticas de un jugador
print(jugador1.estadisticas.puntos)       # 0
print(jugador1.estadisticas.rebotes)      # 0
print(jugador1.estadisticas.asistencias)  # 0

# Actualizar las estadísticas de un jugador
jugador1.estadisticas.puntos = 20
jugador1.estadisticas.rebotes = 10
jugador1.estadisticas.asistencias = 5

# Crear un juego y asignar los equipos
juego = Juego(equipo_local, equipo_visitante)

# Acceder a los equipos en un juego
print(juego.equipo_local.nombre)       # Equipo Local
print(juego.equipo_visitante.nombre)   # Equipo Visitante
