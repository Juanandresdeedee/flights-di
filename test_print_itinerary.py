from fast_flights.model import Airport, CarbonEmission, Flights, SimpleDatetime, SingleFlight


def print_itinerary(flight):
    airports = [flight.flights[0].from_airport.code]
    for segment in flight.flights:
        airports.append(segment.to_airport.code)
    print(" → ".join(airports))

    stops = flight.flights[1:]
    if stops:
        conexiones = [segment.from_airport.code for segment in stops]
        print("Escalas:", len(stops))
        print("Conexión:", ", ".join(conexiones))
    else:
        print("Tipo: Directo")

    for i, segment in enumerate(flight.flights, start=1):
        print(f"  Tramo {i}: {segment.from_airport.code} -> {segment.to_airport.code}")
        print("    Salida:", segment.departure)
        print("    Llegada:", segment.arrival)
        print("    Duración:", segment.duration, "minutos")
        print("    Avión:", segment.plane_type)


def make_segment(origin, destination, departure_time, arrival_time, duration, plane_type):
    return SingleFlight(
        from_airport=Airport(name=origin, code=origin),
        to_airport=Airport(name=destination, code=destination),
        departure=SimpleDatetime(date=(2026, 9, 15), time=departure_time),
        arrival=SimpleDatetime(date=(2026, 9, 15), time=arrival_time),
        duration=duration,
        plane_type=plane_type,
    )


vuelo_directo = Flights(
    type="direct",
    price=250,
    airlines=["American Airlines"],
    flights=[
        make_segment("MIA", "BOG", (8, 0), (10, 30), 210, "Boeing 737"),
    ],
    carbon=CarbonEmission(typical_on_route=180000, emission=175000),
)

vuelo_una_escala = Flights(
    type="multi",
    price=310,
    airlines=["Copa Airlines"],
    flights=[
        make_segment("MIA", "PTY", (7, 0), (9, 15), 135, "Boeing 737"),
        make_segment("PTY", "BOG", (10, 30), (12, 0), 90, "Embraer 190"),
    ],
    carbon=CarbonEmission(typical_on_route=190000, emission=200000),
)

vuelo_dos_escalas = Flights(
    type="multi",
    price=280,
    airlines=["LATAM"],
    flights=[
        make_segment("MIA", "PTY", (6, 0), (8, 15), 135, "Airbus A320"),
        make_segment("PTY", "LIM", (9, 30), (12, 0), 150, "Airbus A319"),
        make_segment("LIM", "BOG", (13, 15), (15, 30), 135, "Airbus A320"),
    ],
    carbon=CarbonEmission(typical_on_route=210000, emission=225000),
)

print("=== Prueba 1: vuelo directo (MIA -> BOG) ===")
print_itinerary(vuelo_directo)

print("\n=== Prueba 2: vuelo con una escala (MIA -> PTY -> BOG) ===")
print_itinerary(vuelo_una_escala)

print("\n=== Prueba 3: vuelo con dos escalas (MIA -> PTY -> LIM -> BOG) ===")
print_itinerary(vuelo_dos_escalas)
