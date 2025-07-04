# Flight Logbook Tracker

# A list to store all flight logs
flights = []

def add_flight():
    """Prompt the user for flight details and add to the flights list."""
    # TODO: Ask for flight details (date, aircraft, hours, etc.)
    # TODO: Create a dictionary and append it to the flights list
    pass

def view_flights():
    """Display all logged flights."""
    # TODO: Loop through the flights list and print each flight
    pass

def save_flights():
    """Save the flight log to a file."""
    # TODO: Use JSON to save flights to a file
    pass

def load_flights():
    """Load the flight log from a file."""
    # TODO: Read JSON file and load into flights list
    pass

def main():
    """Main menu loop."""
    # TODO: Load flights from file if it exists
    while True:
        print("\nFlight Logbook Menu")
        print("1. Add Flight")
        print("2. View Flights")
        print("3. Save Flights")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_flight()
        elif choice == "2":
            view_flights()
        elif choice == "3":
            save_flights()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
