class Vehicle:
    def __init__(self, number, vtype):
        self.number = number
        self.vtype = vtype
        self.entry_time = 0
class ParkingSlot:
    def __init__(self, slot_id):
        self.slot_id = slot_id
        self.vehicle = None
    
    def is_empty(self):
        return self.vehicle == None
class ParkingManager:
    def __init__(self, total_slots, rate_per_hour):
        self.slots = []
        for i in range(1, total_slots + 1):
            self.slots.append(ParkingSlot(i))
        self.rate = rate_per_hour
    def park_vehicle(self, number, vtype, entry_time):
        for slot in self.slots:
            if slot.is_empty():
                v = Vehicle(number, vtype)
                v.entry_time = entry_time
                slot.vehicle = v
                print("Vehicle parked at Slot", slot.slot_id)
                return slot.slot_id
        print("No slots available")
        return None
    def remove_vehicle(self, slot_id, exit_time):
        slot = self.slots[slot_id - 1]
        if slot.vehicle == None:
            print("Slot is already empty")
            return
        hours = exit_time - slot.vehicle.entry_time
        fee = hours * self.rate
        print("Vehicle:", slot.vehicle.number)
        print("Hours parked:", hours)
        print("Parking fee:", fee)
        slot.vehicle = None
pm = ParkingManager(5, 20)
slot = pm.park_vehicle("AP09AB1234", "Car", 10)
pm.remove_vehicle(slot, 14)  