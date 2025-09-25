from core.vehicle import Vehicle

class Scooter(Vehicle):
    def __init__(self, is_functional, battery_level):
        super().__init__(is_functional)
        assert 0 <= battery_level <= 100, "Battery range is valid between 0 - 100"
        self.battery_level = battery_level

    def __str__(self):
        return f"Scooter ID: {self.id} | Status: {'Occupied' if self.is_occupied else 'Free'} | Battery: Battery: {self.battery_level}%"

    def ride(self, distance_in_km):
        assert self.is_functional, "Cannot ride a non-functional scooter."

        battery_drain_rate = 1
        battery_drain = distance_in_km * battery_drain_rate
        self.battery_level -= battery_drain

        if self.battery_level < 0:
            self.battery_level = 0
            self.is_functional = False
            return False
        
        return True

    def charge(self):
        self.battery_level = 100
