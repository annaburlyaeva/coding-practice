class Elevator:
    def __init__(self, id):
        self.id = id
        self.current_floor = 0
        self.destination = None
        self.direction = 1  # 1 for up, -1 for down
        self.stops = set()  # Set of floors where elevator should stop

    def move(self):
        if self.destination is not None:
            if self.current_floor < self.destination:
                self.current_floor += 1
            elif self.current_floor > self.destination:
                self.current_floor -= 1
            else:
                self.stops.discard(self.destination)
                self.destination = None

    def add_stop(self, floor):
        self.stops.add(floor)

    def set_destination(self, destination):
        self.destination = destination
        if destination > self.current_floor:
            self.direction = 1
        elif destination < self.current_floor:
            self.direction = -1


class ElevatorControlSystem:
    def __init__(self, num_elevators):
        self.elevators = [Elevator(i) for i in range(num_elevators)]

    def request_elevator(self, floor):
        # Choose the nearest available elevator
        nearest_elevator = min(self.elevators, key=lambda elevator: abs(
            elevator.current_floor - floor))
        nearest_elevator.set_destination(floor)
        nearest_elevator.add_stop(floor)

    def step(self):
        for elevator in self.elevators:
            elevator.move()


# Usage example:
ecs = ElevatorControlSystem(
    4)  # Initialize elevator control system with 4 elevators
ecs.request_elevator(3)  # Request an elevator to floor 3
ecs.step()  # Move elevators one step
