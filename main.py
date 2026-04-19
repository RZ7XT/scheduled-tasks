from data_manager import DataManager
from pprint import pprint
from datetime import datetime, timedelta
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

notification_manager = NotificationManager()

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

today = datetime.today().date()
tomorrow = today + timedelta(days=1)
six_months_from_today = today + timedelta(hours=4392)

flight_search = FlightSearch()
for destination in sheet_data:
    pprint(f"Getting flights for {destination['city']}...")
    my_flight_data = flight_search.check_flights(origin_city_code="AMM",
                                destination_city_code=destination['iataCode'],
                                from_time=tomorrow,
                                to_time=six_months_from_today)
    cheapest_flight = find_cheapest_flight(my_flight_data, return_date=six_months_from_today)
    pprint(f"{destination['city']}: {cheapest_flight.price} JOD")

    if cheapest_flight.price != "N/A" and int(cheapest_flight.price) < int(destination["lowestPrice"]):
        pprint(f"Lower price flight found to {destination['city']}!")
        data_manager.update_lowest_price(destination["id"], cheapest_flight.price)
        notification_manager.send_telegram_message(f"Low price alert for {destination['city']}!\n\n Only {cheapest_flight.price} JOD to travel from AMM to {destination["iataCode"]}, on {tomorrow.strftime("%Y/%m/%d")} --> {six_months_from_today.strftime("%Y/%m/%d")}")
