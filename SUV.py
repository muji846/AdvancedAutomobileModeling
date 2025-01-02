from Automobile import Automobile


class SUV(Automobile):
    def __init__(self, type):
        super().__init__(type)
        self.fuel = 50  # initialize fuel

    def increase_speed(self):
        if self.speed + 8 <= 100:  # Assuming max speed limit is 100
            self.speed += 8
            print(f"Speed increased to {self.speed}")
        else:
            print("Speed cannot exceed 100")

    def decrease_speed(self):
        if self.speed - 8 >= 0:
            self.speed -= 8
            print(f"Speed decreased to {self.speed}")
        else:
            print("Speed cannot go below 0")

    def move(self):
        if self.fuel > 0:
            # Assuming the speed is in kilometers per hour and time duration is 1 second for simplification
            distance = self.speed * (1 / 3600)  # distance = speed * time
            self.position.x = self.position.x + self.direction.x * distance
            self.position.y = self.position.y + self.direction.y * distance
            self.fuel = self.fuel - distance * (1.0 / 6)  # Consuming fuel
            print(f"Moved to ({self.position.x}, {self.position.y}) with remaining fuel {self.fuel}")
        else:
            print("Not enough fuel to move")
