from core.scooter import Scooter
from core.vehicle import Vehicle

def main():
    """
    This is the main function for the electric scooter sharing application.
    
    The final solution will include classes for Scooter, Station, and Subscriber,
    along with logic to simulate renting and returning scooters.
    """
    print("Electric Scooter App is running!")
    
    scooter1 = Scooter(is_functional=True, battery_level=100)
    print(f"Created a new scooter: {scooter1}")

    distance = 10
    print(f"Riding scooter 1 for {distance} km...")
    scooter1.ride(distance)
    print(f"Scooter 1 status after ride: {scooter1}")

if __name__ == "__main__":
    main()
