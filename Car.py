from Automobile import Automobile


class Car(Automobile):
    def __init__(self, type):
        super().__init__(type)
        self.fuel = 30  # initialize fuel

    def set_type(self, type):
        self.type = type

    def turn_left(self):
        print("Turning left by 5 degrees")
        self.direction.rotate_direction(5)

    def turn_right(self):
        print("Turning right by 5 degrees")
        self.direction.rotate_direction(-5)

    def increase_speed(self):
        if self.speed + 10 <= 120:  # Assuming max speed limit is 120
            self.speed += 10
            print(f"Speed increased to {self.speed}")
        else:
            print("Speed cannot exceed 120")

    def decrease_speed(self):
        if self.speed - 10 >= 0:
            self.speed -= 10
            print(f"Speed decreased to {self.speed}")
        else:
            print("Speed cannot go below 0")

    def move(self):
        if self.fuel > 0:
            # Assuming the speed is in kilometers per hour and time duration is 1 second for simplification
            distance = self.speed * (1 / 3600)  # distance = speed * time
            self.position.x = self.position.x + self.direction.x * distance
            self.position.y = self.position.y + self.direction.y * distance
            self.fuel = self.fuel - distance * (1.0 / 8)  # Consuming fuel
            print(f"Moved to ({self.position.x}, {self.position.y}) with remaining fuel {self.fuel}")
        else:
            print("Not enough fuel to move")
