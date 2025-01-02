Overview of the Automobile Modeling Project

This Python project models four types of automobiles—Car, SUV, Bus, and Truck—using object-oriented programming (OOP) principles.
Each vehicle type is implemented as a class inheriting from a base class (Automobile or AutomobileWithManualXmission).
The project focuses on specific features such as gear-based speed control, manual transmission handling, and fuel consumption tracking.
Key challenges included ensuring adherence to constraints like speed limits for each gear and initializing all vehicles with maximum fuel capacity.
Testing was conducted to validate functionality and ensure the expected behavior for all vehicle types.

# Automobile Modeling Project

## Overview
This project models four types of automobiles—Car, SUV, Bus, and Truck—using Python and object-oriented programming (OOP) principles.
The goal was to implement unique behaviors for each vehicle type, such as handling manual transmission, managing speed and gear constraints, and tracking fuel consumption.
Each class inherits from a provided base class and adheres to strict constraints defined in the project requirements.

## Features
- **Vehicle Types:** Car, SUV, Bus, and Truck with unique attributes and behaviors.
- **Manual Transmission:** Implemented gear-based speed control for Bus and Truck.
- **Fuel Management:** Vehicles initialize with maximum fuel and calculate consumption during movement.
- **Class Design:** Each vehicle type is implemented as a class inheriting from a base class.
- **OOP Principles:** Inheritance, method overriding, and encapsulation used to ensure modularity and reusability.

## How to Run
1. Clone the repository to your local machine.
2. Ensure that `Automobile.py` and `AutomobileTest.py` are included in the project folder.
3. Run the Python program:
   ```bash
   python main.py
