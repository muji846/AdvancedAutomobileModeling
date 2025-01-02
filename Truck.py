from Automobile import AutomobileWithManualTransmission

class Truck(AutomobileWithManualTransmission):
    def __init__(self, type=''):
        super().__init__(type)
        self.fuel = 100  # initialize fuel

    def increase_speed(self):
        self.speed += 4
        # Handle different gear positions
        if self.gear_position == 0:
            print("Error: You need to increase your gear first.")
        elif self.gear_position == 1:
            # Handle gear position 1
            if self.speed > 20:
                self.speed = 20
                print("Error: Speed cannot exceed current gear's maximum speed limit.")
        elif self.gear_position == 2:
            # Handle gear position 2
            if self.speed > 30:
                self.speed = 30
                print("Error: Speed cannot exceed current gear's maximum speed limit.")
        elif self.gear_position == 3:
            # Handle gear position 3
            if self.speed > 45:
                self.speed = 45
                print("Error: Speed cannot exceed current gear's maximum speed limit.")
        elif self.gear_position == 4:
            # Handle gear position 4
            if self.speed > 50:
                self.speed = 50
                print("Error: Speed cannot exceed current gear's maximum speed limit.")
        elif self.gear_position == 5:
            # Handle gear position 5
            if self.speed > 60:
                self.speed = 60
                print("Error: Speed cannot exceed current gear's maximum speed limit.")
        else:
            # Handle default case
            pass

    def decrease_speed(self):
        self.speed -= 4
        # Handle different gear positions
        if self.gear_position == 0:
            print("Error: You need to increase your gear first.")
        elif self.gear_position == 1:
            # Handle gear position 1
            if self.speed < 0:
                self.speed = 0
                print("Error: Speed cannot exceed current gear's minimum speed limit.")
        elif self.gear_position == 2:
            # Handle gear position 2
            if self.speed < 10:
                self.speed = 10
                print("Error: Speed cannot exceed current gear's minimum speed limit.")
        elif self.gear_position == 3:
            # Handle gear position 3
            if self.speed < 25:
                self.speed = 25
                print("Error: Speed cannot exceed current gear's minimum speed limit.")
        elif self.gear_position == 4:
            # Handle gear position 4
            if self.speed < 35:
                self.speed = 35
                print("Error: Speed cannot exceed current gear's minimum speed limit.")
        elif self.gear_position == 5:
            # Handle gear position 5
            if self.speed < 50:
                self.speed = 50
                print("Error: Speed cannot exceed current gear's minimum speed limit.")
        else:
            # Handle default case
            pass

    def move(self):
        if self.gear_position == 0:
            print("Error: You need to increase your gear first.")
        elif self.fuel <= 0:
            print("Not enough fuel to move")
        else:
            # Assuming the speed is in kilometers per hour and time duration is 1 second for simplification
            distance = self.speed * (1 / 3600)  # distance = speed * time
            self.position.x += self.direction.x * distance
            self.position.y += self.direction.y * distance
            self.fuel -= distance * 0.5  # Consuming fuel
            print(f"Moved to ({self.position.x}, {self.position.y}) with remaining fuel {self.fuel}")

    def shift_gear_up(self):
        if self.gear_position < 5:
            self.gear_position += 1
            print(f"Shifted gear up to {self.gear_position}")
        else:
            print("Error: Already in the highest gear.")

    def shift_gear_down(self):
        if self.gear_position > 1:  # Adjusted the condition to prevent shifting to gear 0
            self.gear_position -= 1
            print(f"Shifted gear down to {self.gear_position}")
        else:
            print("Error: Already in the lowest gear.")
