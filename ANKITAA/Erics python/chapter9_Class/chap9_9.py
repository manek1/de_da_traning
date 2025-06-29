#9-9. Battery Upgrade: Use the final version of electric_car.py from this section.
#Add a method to the Battery class called upgrade_battery(). This method
#should check the battery size and set the capacity to 85 if it isn’t already.
#Make an electric car with a default battery size, call get_range() once, and
#then call get_range() a second time after upgrading the battery. You should
#see an increase in the car’s range.

# Car class (general)
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}"

# Battery class (used by ElectricCar)
class Battery:
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range_estimate = 240
        elif self.battery_size == 85:
            range_estimate = 270
        else:
            range_estimate = 200  # fallback/default
        print(f"This car can go about {range_estimate} miles on a full charge.\n")

    def upgrade_battery(self):
        if self.battery_size < 85:
            print("Upgrading the battery to 85 kWh...")
            self.battery_size = 85
        else:
            print("Battery already upgraded.\n")

# ElectricCar class (inherits from Car and uses Battery)
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()  # composition

# Creating an electric car instance
my_tesla = ElectricCar("Tesla", "Model S", 2024)

# Initial range
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# Upgrade battery
my_tesla.battery.upgrade_battery()

# Range after upgrade
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()