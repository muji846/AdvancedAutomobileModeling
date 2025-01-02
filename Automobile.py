import math


class Coordinate:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def rotate_direction(self, angle):
        theta = (math.pi * angle) / 180
        px = self.x * math.cos(theta) - self.y * math.sin(theta)
        py = self.x * math.sin(theta) + self.y * math.cos(theta)
        self.x = px
        self.y = py


class Automobile:
    def __init__(self, type='', position=Coordinate(), direction=Coordinate(), speed=0, fuel=0):
        self.type = type
        self.position = position
        self.direction = direction
        self.speed = speed
        self.fuel = fuel

    def set_initial_position(self, init_pos):
        self.position = init_pos

    def set_initial_direction(self, direction):
        self.direction = direction

    def get_type(self):
        return self.type

    def get_fuel(self):
        return self.fuel

    def get_speed(self):
        return self.speed

    def get_position(self):
        return self.position

    def get_direction(self):
        return self.direction

    def turn_left(self, angle):
        self.direction.rotate_direction(angle)

    def turn_right(self, angle):
        self.direction.rotate_direction(-angle)

    def increase_speed(self, amount):
        self.speed += amount

    def decrease_speed(self, amount):
        self.speed -= amount

    def move(self, time, fuel_efficiency):
        amount = self.speed * (time / 3600)  # Convert time to hours
        self.position.x += self.direction.x * amount
        self.position.y += self.direction.y * amount
        self.fuel -= amount * fuel_efficiency


class AutomobileWithManualTransmission(Automobile):
    def __init__(self, type=''):
        super().__init__(type)
        self.gear_position = 0

    def shift_gear_up(self):
        if self.gear_position < 5:
            self.gear_position += 1

    def shift_gear_down(self):
        if self.gear_position > 0:
            self.gear_position -= 1

    def get_gear_position(self):
        return self.gear_position
