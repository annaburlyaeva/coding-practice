# Design parking lot

class Vehicle:
    def __init__(self, license_plate, size):
        self.license_plate = license_plate
        self.size = size  # Size of the vehicle (e.g., 'compact', 'midsize', 'large')


class ParkingSpot:
    def __init__(self, spot_number, size):
        self.spot_number = spot_number
        self.size = size  # Size of the parking spot (e.g., 'compact', 'midsize', 'large')
        self.vehicle = None  # Initially, no vehicle parked in the spot


class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity  # Total number of parking spots
        self.available_spots = set()  # List of available parking spots
        self.parking_spots = {}  # Dictionary to map spot numbers to parking spots

        # Initialize parking spots
        for spot_number in range(1, capacity + 1):
            parking_spot = ParkingSpot(spot_number, size=None)
            self.available_spots.add(parking_spot)
            self.parking_spots[spot_number] = parking_spot

    def park_vehicle(self, vehicle):
        for spot in self.available_spots:
            if spot.size == vehicle.size:
                spot.vehicle = vehicle
                self.available_spots.remove(spot)
                return spot.spot_number
        return -1  # No available spot for the vehicle

    def unpark_vehicle(self, spot_number):
        if spot_number in self.parking_spots:
            spot = self.parking_spots[spot_number]
            spot.vehicle = None
            self.available_spots.add(spot)
            return True
        else:
            return False  # Spot number does not exist


# Example usage:
parking_lot = ParkingLot(capacity=50)
vehicle1 = Vehicle("ABC123", "compact")
vehicle2 = Vehicle("XYZ456", "large")

spot_number1 = parking_lot.park_vehicle(vehicle1)
print("Vehicle 1 parked in spot number:", spot_number1)

spot_number2 = parking_lot.park_vehicle(vehicle2)
print("Vehicle 2 parked in spot number:", spot_number2)

print("Unparking vehicle 1 from spot number:", spot_number1)
parking_lot.unpark_vehicle(spot_number1)

spot_number3 = parking_lot.park_vehicle(vehicle1)
print("Vehicle 1 parked again in spot number:", spot_number3)
