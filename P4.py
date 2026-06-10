class Guest:
    def __init__(self, gid, name):
        self.gid = gid
        self.name = name
class Room:
    def __init__(self, room_no, room_type, price):
        self.room_no = room_no
        self.room_type = room_type
        self.price = price
        self.booked = False
class Reservation:
    def __init__(self, guest, room, nights):
        self.guest = guest
        self.room = room
        self.nights = nights
    def total_amount(self):
        return self.room.price * self.nights
    def print_bill(self):
        print("HOTEL BILL")
        print("Guest:", self.guest.name)
        print("Room:", self.room.room_no, "-", self.room.room_type)
        print("Nights:", self.nights)
        print("Price per night:", self.room.price)
        print("Total Amount:", self.total_amount())
room1 = Room(101, "Deluxe", 2000)
guest1 = Guest("G1", "Amit")

if not room1.booked:
    room1.booked = True
    res = Reservation(guest1, room1, 3)
    res.print_bill()
else:
    print("Room already booked")