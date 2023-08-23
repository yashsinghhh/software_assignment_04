class Flight:
    def __init__(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price


class Table:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_by_city(self, city):
        return [flight for flight in self.flights if flight.source == city]

    def search_for_city(self, city):
        return [flight for flight in self.flights if flight.destination == city]

    def search_by_source_destination(self, source, destination):
        return [flight for flight in self.flights if flight.source == source and flight.destination == destination]

    def display_flights(self, flights):
        if not flights:
            print("No flights found.")
            return
        print("Flight ID\tFrom\tTo\tPrice")
        for flight in flights:
            print(
                f"{flight.flight_id}\t{flight.source}\t{flight.destination}\t{flight.price}")


def main():
    flight_table = Table()

    flight_table.add_flight(Flight("AI161E90", "BLR", "BOM", 5600))
    flight_table.add_flight(Flight("BR161F91", "BOM", "BBI", 6750))
    flight_table.add_flight(Flight("AI161F99", "BBI", "BLR", 8210))
    flight_table.add_flight(Flight("VS171E20", "JLR", "BBI", 5500))
    flight_table.add_flight(Flight("AS171G30", "HYD", "JLR", 4400))
    flight_table.add_flight(Flight("AI131F49", "HYD", "BOM", 3499))

    while True:
        print("\nSearch Options:")
        print("1. Destination City")
        print("2. Departing City")
        print("3. Flights between two given cities")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            city = input("Enter the city name: ")
            found_flights = flight_table.search_for_city(city)
            flight_table.display_flights(found_flights)

        elif choice == "2":
            city = input("Deaparting City name: ")
            found_flights = flight_table.search_by_city(city)
            flight_table.display_flights(found_flights)

        elif choice == "3":
            source = input("Departing name: ")
            destination = input("Destination City name: ")
            found_flights = flight_table.search_by_source_destination(
                source, destination)
            flight_table.display_flights(found_flights)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
