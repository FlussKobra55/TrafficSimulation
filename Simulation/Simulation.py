from .Road import Road
from copy import deepcopy
from .VehicleGenerator import VehicleGenerator
from .TrafficSignal import TrafficSignal


class Simulation:
    vehiclesPassed = 0;
    vehiclesPresent = 0;
    isPaused = False;

    trafficmode = 'notgiven'

    def __init__(self, trafficmode, config={}):
        # Set default configuration
        self.set_default_config()

        self.trafficmode = trafficmode

        # Update configuration
        for attr, val in config.items():
            setattr(self, attr, val)

    def set_default_config(self):
        self.t = 0.0  # Time keeping
        self.frame_count = 0  # Frame count keeping
        self.dt = 1 / 60  # Simulation time step
        self.roads = []  # Array to store roads
        self.generators = []
        self.traffic_signals = []

    def create_road(self, start, end):
        road = Road(start, end)
        self.roads.append(road)
        return road

    def create_roads(self, road_list):
        for road in road_list:
            self.create_road(*road)

    def create_gen(self, config={}):
        gen = VehicleGenerator(self, config)
        self.generators.append(gen)
        return gen

    def create_signal(self, roads, config={}):
        roads = [[self.roads[i] for i in road_group] for road_group in roads]
        sig = TrafficSignal(roads, self.trafficmode, config)
        self.traffic_signals.append(sig)
        return sig

    def update(self):
        # Update every road
        for road in self.roads:
            road.update(self.dt)

        # Add vehicles
        for gen in self.generators:
            gen.update()

        for signal in self.traffic_signals:
            signal.update(self)

        # Check roads for out of bounds vehicle
        for road in self.roads:
            # If road has no vehicles, continue
            if len(road.vehicles) == 0: continue
            # If not
            vehicle = road.vehicles[0]
            # If first vehicle is out of road bounds
            if vehicle.x >= road.length:
                # If vehicle has a next road
                if vehicle.current_road_index + 1 < len(vehicle.path):
                    # Update current road to next road
                    vehicle.current_road_index += 1
                    # Create a copy and reset some vehicle properties
                    new_vehicle = deepcopy(vehicle)
                    new_vehicle.x = 0
                    # Add it to the next road
                    next_road_index = vehicle.path[vehicle.current_road_index]
                    self.roads[next_road_index].vehicles.append(new_vehicle)
                else:
                    Simulation.vehiclesPassed += 1
                # In all cases, remove it from its road
                road.vehicles.popleft()

                # if vehicle reached the end of the path
                # if vehicle.current_road_index + 1 == len(vehicle.path):
                #     Simulation.vehiclesPassed += 1
                # print("Vehicle passed: " + str(Simulation.vehiclesPassed))

        # Check for the number of vehicles present
        Simulation.vehiclesPresent = 0
        for road in self.roads:
            Simulation.vehiclesPresent += len(road.vehicles)

        # Increment time
        self.t += self.dt
        self.frame_count += 1

    def run(self, steps):
        for _ in range(steps):
            self.update()

    def pause(self):
        self.isPaused = True

    def resume(self):
        self.isPaused = False
