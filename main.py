import json
import requests

flights = []

def load_flights():
    global flights
    try:
        with open("flights.json", "r") as file:
            flights = json.load(file)
    except FileNotFoundError:
        flights = []

def save_flights():
    with open("flights.json", "w") as file:
        json.dump(flights, file, indent=4)

def fetch_metar(icao):
    print(f"Fetching METAR for {icao}...")
    # Replace 'YOUR_API_KEY' with your actual API key from avwx.rest
    headers = {"Authorization": "YOUR_API_KEY"}
    url = f"https://avwx.rest/api/metar/{icao}?format=json"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("raw", "No METAR data available")
    else:
        return "Failed to retrieve METAR data"

def add_flight():
    flight = {
        "date": input("Date (YYYY-MM-DD): "),
        "aircraft": input("Aircraft Type: "),
        "hours": float(input("Flight Hours: ")),
        "departure": input("Departure ICAO: "),
        "arrival": input("Arrival ICAO: "),
        "remarks": input("Remarks: ")
    }
    metar = fetch_metar(flight["departure"])
    flight["weather_metar"] = metar
    flights.append(flight)
    save_flights()
    print("Flight added and saved.")

def view_flights():
    for i, flight in enumerate(flights, 1):
        print(f"Flight {i}: {flight}")

def main():
    load_flights()
    while True:
        print("\n1. Add Flight\n2. View Flights\n3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_flight()
        elif choice == "2":
            view_flights()
        elif choice == "3":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
