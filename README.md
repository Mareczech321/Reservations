# Room Reservation System

## Overview
The Room Reservation System is a Python-based application that allows users to:
- Add room reservations for specific dates and time slots.
- View all existing reservations.
- Cancel a reservation by providing its ID.

The system ensures that reservations are validated and conflict-free.

---

## Features
1. **Add Reservation**: 
   - Users can book a room by entering their name, the room name, date, and time slot.
   - The system validates the reservation to ensure:
     - The date is in the future.
     - The time slot is valid (start time is before end time).
     - The room is available during the specified time slot.

2. **Show Reservations**:
   - Displays a list of all reservations sorted by date.
   - Each reservation includes the ID, room name, date, time, and the name of the person who booked it.

3. **Cancel Reservation**:
   - Users can cancel a reservation by entering its ID.
   - Before prompting for an ID, the system displays all available reservation IDs along with their details for easy reference.

4. **Error Handling**:
   - Ensures input is valid (e.g., correct date and time formats, valid reservation IDs).
   - Provides user-friendly error messages for invalid operations.

5. **Exit**:
   - Allows users to exit the application safely.

---

## How to Run
### Prerequisites
- Python 3.x installed on your system.

### Files
1. `main.py`: The main script containing the application logic.
2. `user.py`: A simple module to represent the user making a reservation.

### Steps
1. Clone or download the repository.
2. Open a terminal and navigate to the project directory.
3. Run the application:
   ```bash
   python main.py
   ```

# Usage
## Menu Options
### Add Reservation:

Enter your name, room name, date (in YYYY-MM-DD format), start time (in HH:MM format), and end time.
- The system will confirm if the reservation was successful or display an error message.
### Show Reservations:

- Displays all reservations sorted by date.
### Cancel Reservation:

- The system shows all existing reservation IDs.
Enter a valid ID to cancel the corresponding reservation.
### Exit:

- Terminates the program.

# Notes
- Reservations are stored in memory during the runtime of the program.
- Future versions could include persistent storage or a graphical interface.