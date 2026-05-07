from data_manager import DataManager
from datetime import datetime, timedelta, date
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

#Personal: Countdown Until Event.

day_in_question = date(2026, 7, 23)

now = date.today()

difference = day_in_question - now
if difference.days >= 0:
    notification_manager.send_telegram_message(f"{difference.days} Days Left Until Wizari.")

#--------------------------------------------------------------------------------------------

notification_manager = NotificationManager()

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

today = datetime.today().date()
tomorrow = today + timedelta(days=1)
one_week_from_today = today + timedelta(hours=132)

flight_search = FlightSearch()
for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    my_flight_data = flight_search.check_flights(origin_city_code="AMM",
                                destination_city_code=destination['iataCode'],
                                from_time=tomorrow,
                                to_time=one_week_from_today)
    cheapest_flight = find_cheapest_flight(my_flight_data, return_date=one_week_from_today)
    print(f"{destination['city']}: {cheapest_flight.price} JOD")

    if cheapest_flight.price != "N/A" and int(cheapest_flight.price) < int(destination["lowestPrice"]):
        print(f"Lower price flight found to {destination['city']}!")
        data_manager.update_lowest_price(destination["id"], cheapest_flight.price)
        notification_manager.send_telegram_message(f"Low price alert for {destination['city']}!\n\n Only {cheapest_flight.price} JOD to travel from AMM to {destination["iataCode"]}, on {tomorrow.strftime("%Y/%m/%d")} --> {one_week_from_today.strftime("%Y/%m/%d")}")
        
