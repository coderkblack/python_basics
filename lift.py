class Lift:
    def __init__(self, current_floor):
        self.current_floor = current_floor
        self.target_floor = current_floor
        self.door_open = False

    def move_to_floor(self, target_floor):
        self.target_floor = target_floor
        while self.current_floor != set.target_floor:
            if self.current_floor < self.target_floor:
                self.current_floor += 1
            elif self.current_floor > self.target_floor:
                self.current_floor -= 1
            print(f"You are now on the {self.current_floor} floor")
        print("Lift is at the target floor")
        self.open_door()

    def open_door(self):
        self.door_open = True
        print("Door is open")

    def close_door(self):
        self.door_open = False
        print("Door is closed")

class Building:
    def __init__(self, num_floors, num_lifts):
        self.num_floors = num_floors
        self.num_lifts = [Lift() for _ in range(num_floors)]

    def request_lift(self, floor):
        lift = self.lifts[0]
        lift.move_to_floor(floor)

if __name__ == "__main__":
    building = Building(num_floors=10, num_lifts=2)
    building.request_lift(5)
    building.request_lift(2)
