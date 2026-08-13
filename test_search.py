from fast_flights import FlightQuery, Passengers, create_query, get_flights


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


print("✈️ FLIGHT FINDER")
print("------------------")

origin = input("Aeropuerto de origen: ").upper()
destination = input("Aeropuerto de destino: ").upper()
date = input("Fecha (YYYY-MM-DD): ")
budget = int(input("Presupuesto máximo en USD: $"))

query = create_query(
    flights=[
        FlightQuery(
            date=date,
            from_airport=origin,
            to_airport=destination,
        )
    ],
    seat="economy",
    trip="one-way",
    passengers=Passengers(adults=1),
    language="en-US",
    currency="USD",
)

print("\n🔎 Buscando vuelos...")

try:
    results = get_flights(query)
except Exception as error:
    print("\n⚠️ No pude procesar la respuesta de Google Flights.")
    print("El formato de respuesta puede haber cambiado.")
    print("Error técnico:", error)
    raise SystemExit(1)

for flight in results:
    print("----------------------------")
    print("Aerolínea:", flight.airlines)
    print("Precio: $", flight.price)
    print_itinerary(flight)

cheapest = min(results, key=lambda flight: flight.price)

print("\n=== 🏆 VUELO MÁS BARATO ===")
print("Aerolínea:", cheapest.airlines)
print("Precio: $", cheapest.price)
print_itinerary(cheapest)

if cheapest.price <= budget:
    print("✅ Encontré un vuelo dentro de tu presupuesto.")
    print("Te sobran: $", budget - cheapest.price)
else:
    print("❌ El vuelo más barato supera tu presupuesto.")
    print("Te faltan: $", cheapest.price - budget)