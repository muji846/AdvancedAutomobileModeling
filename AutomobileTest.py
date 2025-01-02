from Automobile import Coordinate
from Car import Car
from SUV import SUV
from Bus import Bus
from Truck import Truck

def main():
    # Demonstration for Car
    car = Car("Automatic")
    print("Demonstration for Car")
    car.set_initial_position(Coordinate(5, 3))
    car.set_initial_direction(Coordinate(10, 30))
    car.turn_left()
    car.increase_speed()
    car.increase_speed()
    car.increase_speed()
    car.move()
    car.move()
    car.move()
    car.turn_right()
    car.increase_speed()

    # Demonstration for SUV
    suv = SUV("Automatic")
    print("\nDemonstration for SUV")
    suv.set_initial_position(Coordinate(10, 5))
    suv.set_initial_direction(Coordinate(20, 40))
    suv.turn_left(10)  # Pass the angle parameter
    suv.increase_speed()
    suv.increase_speed()
    suv.move()
    suv.move()
    suv.turn_right(10)  # Pass the angle parameter
    suv.decrease_speed()

    # Demonstration for Bus
    bus = Bus("Manual")
    print("\nDemonstration for Bus")
    bus.set_initial_position(Coordinate(15, 10))
    bus.set_initial_direction(Coordinate(30, 60))
    bus.turn_left(15)  # Pass the angle parameter
    bus.increase_speed()
    bus.move()
    bus.move()
    bus.turn_right(15)  # Pass the angle parameter
    bus.decrease_speed()
    bus.move()

    # Demonstration for Truck
    truck = Truck("Manual")
    print("\nDemonstration for Truck")
    truck.set_initial_position(Coordinate(20, 15))
    truck.set_initial_direction(Coordinate(40, 80))
    truck.turn_left(25)  # Pass the angle parameter
    truck.shift_gear_up()  # Shift gear up first
    truck.increase_speed()
    truck.move()
    truck.move()
    truck.turn_right(25)  # Pass the angle parameter
    truck.shift_gear_down()  # Shift gear down before decreasing speed
    truck.decrease_speed()
    truck.move()
    truck.move()
    truck.move()

if __name__ == '__main__':
    main()
