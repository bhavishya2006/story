import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch(debug=True)
notification_manager = NotificationManager()


sheet_data = data_manager.get_destination_data()

ORIGIN_CITY_IATA = "DFW"

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        time.sleep(2)

print(f"Updated sheet data:\n{sheet_data}")

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

customer_data = data_manager.get_customer_emails()
customer_email_list = [row["whatIsYourEmail?"] for row in customer_data]


tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))


for destination in sheet_data:
    print(f"\nSearching direct flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: ${cheapest_flight.price}")

    time.sleep(2)


    if cheapest_flight.price == "N/A":
        print(f"No direct flight to {destination['city']}. Searching indirect flights...")
        stopover_flights = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today,
            is_direct=False
        )
        cheapest_flight = find_cheapest_flight(stopover_flights)
        print(f"Cheapest indirect flight price is: ${cheapest_flight.price}")


    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:

        if cheapest_flight.stops == 0:
            message = (
                f"Low price alert! Only USD {cheapest_flight.price} to fly direct "
                f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
            )
        else:
            message = (
                f"Low price alert! Only USD {cheapest_flight.price} to fly "
                f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                f"with {cheapest_flight.stops} stop(s), departing on {cheapest_flight.out_date} "
                f"and returning on {cheapest_flight.return_date}."
            )

        print(f"✅ Lower price found for {destination['city']}. Sending notifications...")


        notification_manager.send_whatsapp(message_body=message)


        notification_manager.send_emails(email_list=customer_email_list, email_body=message)
    else:
        print(f"No lower price found for {destination['city']}.")
