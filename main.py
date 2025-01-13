import random as rdm
from datetime import datetime
from user import User

reservations: list = []

def occupiedRoom(roomName, date, start, end):
    for reservation in reservations:
        if (
            reservation["Room name"] == roomName
            and reservation["Date"] == date
            and not (
                end <= reservation["Time period start"] or start >= reservation["Time period end"]
            )
        ):
            return False
    return True

def is_future_date(date):
    return datetime.strptime(date, "%Y-%m-%d") > datetime.now()

def is_valid_time_range(start, end):
    return start < end

def add_reservation(user, roomName, date, start, end):
    if not is_future_date(date):
        print("Error: The date must be in the future.")
        return
    if not is_valid_time_range(start, end):
        print("Error: Invalid time range. Start time must be before end time.")
        return
    if not occupiedRoom(roomName, date, start, end):
        print("Error: The room is already reserved for the selected time.")
        return

    reservation_id = rdm.randint(1000, 9999)

    reservations.append({
        "id": reservation_id,
        "user": user.name,
        "Room name": roomName,
        "Date": date,
        "Time period start": start,
        "Time period end": end,
    })
    print(f"Reservation added successfully! Reservation ID: {reservation_id}")

def show_reservations():
    if not reservations:
        print("No reservations found.")
        return

    sorted_reservations = sorted(reservations, key=lambda x: x["Date"])
    for res in sorted_reservations:
        print(
            f"ID: {res['id']}, Reserved by: {res['user']}, Room: {res['Room name']}, Date: {res['Date']}, Time: {res['Time period start']} - {res['Time period end']}"
        )

def cancel_reservation(reservation_id):
    for reservation in reservations:
        if reservation["id"] == reservation_id:
            reservations.remove(reservation)
            print("Reservation canceled successfully.")
            return
    print("Error: Reservation ID not found.")

def main():
    print("Welcome to the Room Reservation System")

    while True:
        print("\nMenu:")
        print("1. Add Reservation")
        print("2. Show Reservations")
        print("3. Cancel Reservation")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            user = User(input("Enter your name: "))            
            roomName = input("Enter room name: ")
            date = input("Enter date (YYYY-MM-DD): ")
            start = input("Enter start time (HH:MM): ")
            end = input("Enter end time (HH:MM): ")
            add_reservation(user, roomName, date, start, end)

        elif choice == "2":
            show_reservations()

        elif choice == "3":
            if not reservations:
                print("No reservations found to cancel.")
            else:
                print("Available Reservation IDs:")
                for res in reservations:
                    print(f"ID: {res['id']}, Room: {res['Room name']}, Date: {res['Date']}")
                try:
                    reservation_id = int(input("Enter reservation ID to cancel: "))
                    cancel_reservation(reservation_id)
                except ValueError:
                    print("Error: Please enter a valid ID.")

        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Error: Invalid choice. Please try again.")

if __name__ == "__main__":
    main()