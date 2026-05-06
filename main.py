seats = 5
bookings = {}

def check_availability():
    print("Available seats:", seats)

def book_ticket():
    global seats
    if seats > 0:
        name = input("Enter name: ")
        age = input("Enter age: ")
        booking_id = len(bookings) + 1
        bookings[booking_id] = {"name": name, "age": age}
        seats -= 1
        print("Booking successful! Your ID is:", booking_id)
    else:
        print("No seats available!")

def view_ticket():
    bid = int(input("Enter booking ID: "))
    if bid in bookings:
        print(bookings[bid])
    else:
        print("Booking not found")

def cancel_ticket():
    global seats
    bid = int(input("Enter booking ID: "))
    if bid in bookings:
        del bookings[bid]
        seats += 1
        print("Ticket cancelled")
    else:
        print("Booking not found")

while True:
    print("\n1.Check Availability")
    print("2.Book Ticket")
    print("3.View Ticket")
    print("4.Cancel Ticket")
    print("5.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        check_availability()
    elif choice == "2":
        book_ticket()
    elif choice == "3":
        view_ticket()
    elif choice == "4":
        cancel_ticket()
    elif choice == "5":
        break
    else:
        print("Invalid choice")
