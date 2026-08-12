from fast_flights import FlightQuery, Passengers, create_query, get_flights

query = create_query(
    flights=[
        FlightQuery(
            date="2026-09-15",
            from_airport="MIA",
            to_airport="BOG",
        )
    ],
    seat="economy",
    trip="one-way",
    passengers=Passengers(adults=1),
    language="en-US",
    currency="USD",
)

results = get_flights(query)

for flight in results:
    segment = flight.flights[0]

    print("----------------------------")
    print("Aerolínea:", flight.airlines)
    print("Precio: $", flight.price)
    print("Origen:", segment.from_airport.code)
    print("Destino:", segment.to_airport.code)
    print("Salida:", segment.departure)
    print("Llegada:", segment.arrival)
    print("Duración:", segment.duration, "minutos")
    print("Avión:", segment.plane_type)



    cheapest = min(results, key=lambda flight: flight.price)

print("\n=== VUELO MÁS BARATO ===")
print("Aerolínea:", cheapest.airlines)
print("Precio: $", cheapest.price)