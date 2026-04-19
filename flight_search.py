import os
from requests_cache import CachedSession


class FlightSearch:
    def __init__(self):
        self.SERPAPI = os.environ.get("SERPAPI_API_KEY")

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        params = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time,
            "return_date": to_time,
            "type": "1",
            "adults": "1",
            "currency": "JOD",
            "deep_search": "true",
            "api_key": self.SERPAPI
        }
        session = CachedSession(expire_after=43200)
        flights = session.get("https://serpapi.com/search?engine=google_flights", params=params)
        if flights.status_code != 200:
            print(f"check_flights() response code: {flights.status_code}"
                  f"Error Details: {flights.text}")
            return None

        data = flights.json()
        if "error" in data:
            print(f"API error: {data['error']}")
            return None
        return data
