class FlightData:

    def __init__(self, price, origin_airport, destination_airport, out_date, return_date, stops):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops

def find_cheapest_flight(data):

    if data is None or not data['data']:
        print("No flight data")
        return FlightData(
            price="N/A",
            origin_airport="N/A",
            destination_airport="N/A",
            out_date="N/A",
            return_date="N/A",
            stops="N/A"
        )

    # Initialize from first flight
    first_flight = data['data'][0]
    lowest_price = float(first_flight["price"]["grandTotal"])
    segments_outbound = first_flight["itineraries"][0]["segments"]
    nr_stops = len(segments_outbound) - 1

    origin = segments_outbound[0]["departure"]["iataCode"]
    destination = segments_outbound[-1]["arrival"]["iataCode"]
    out_date = segments_outbound[0]["departure"]["at"].split("T")[0]
    return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

    cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date, nr_stops)

    for flight in data["data"]:
        price = float(flight["price"]["grandTotal"])
        segments_outbound = flight["itineraries"][0]["segments"]
        nr_stops = len(segments_outbound) - 1

        if price < lowest_price:
            lowest_price = price
            origin = segments_outbound[0]["departure"]["iataCode"]
            destination = segments_outbound[-1]["arrival"]["iataCode"]
            out_date = segments_outbound[0]["departure"]["at"].split("T")[0]
            return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

            cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date, nr_stops)

            print(f"Lowest price to {destination} is ${lowest_price}")  # <-- USD

    return cheapest_flight
