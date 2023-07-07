#! /usr/bin/env python3

import os
import math
import json
import logging
from typing import Dict, List, TextIO

# If you add or upgrade any pip packages, please specify in `requirements.txt`

# Each Nest has this many Zips
NUM_ZIPS = 10

# Each Zip can carry between 1 and this many packages per flight
# Note: a Zip can deliver more than 1 package per stop
MAX_PACKAGES_PER_ZIP = 3

# Zips fly a constant groundspeed (m/s)
ZIP_SPEED_MPS = 30

# Zips can fly a total roundtrip distance (m)
ZIP_MAX_CUMULATIVE_RANGE_M = 160 * 1000  # 160 km -> meters

# The two acceptable priorities
EMERGENCY = "Emergency"
RESUPPLY = "Resupply"

# Setup logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Setup simulation result object
simulation_result = {}

# You shouldn't need to modify this class
class Hospital:
    def __init__(self, name: str, north_m: int, east_m: int):
        self.name = name
        self.north_m = north_m
        self.east_m = east_m

    @staticmethod
    def load_from_csv(f: TextIO) -> Dict[str, "Hospital"]:
        """Reads and processes a CSV file object that conforms to the
        hospital.csv schema defined in README.md.

        Args:
            f (file_object): CSV file object to read into a dict.

        Returns:
            dict: Hospitals and their coordinates.
        """
        hospitals = {}
        for line in f.readlines():
            fields = [values.strip() for values in line.split(",")]
            name = fields[0]
            hospitals[name] = Hospital(
                name=name,
                north_m=int(fields[1]),
                east_m=int(fields[2]),
            )
        return hospitals


# You shouldn't need to modify this class
class Order:
    def __init__(self, time: int, hospital: Hospital, priority: str):
        self.time = time
        self.hospital = hospital
        self.priority = priority

    @staticmethod
    def load_from_csv(f: TextIO, hospitals: Dict[str, Hospital]) -> List["Order"]:
        """Reads and processes a CSV file object that conforms to the
        orders.csv schema defined in README.md.
        Ok to assume the orders are sorted.

        Args:
            f (file_object): CSV file object to read into a dict.
            hospitals (dict): mapping of hospital name to Hospital objects

        Returns:
            list: Order objects.
        """
        orders = []
        for line in f.readlines():
            fields = [values.strip() for values in line.split(",")]
            orders.append(
                Order(
                    time=int(fields[0]),
                    hospital=hospitals[fields[1]],
                    priority=fields[2],
                )
            )
        return orders


# Feel free to extend as needed
class Flight:
    def __init__(self, launch_time: int, return_time: int, orders: List[Order]):
        self.launch_time = launch_time
        self.return_time = return_time
        self.orders = orders

    def __str__(self) -> str:
        orders_str = "->".join([o.hospital.name for o in self.orders])
        return f"<Flight @ {self.launch_time} to {orders_str}>"

class ZipScheduler:
    def __init__(
        self,
        hospitals: Dict[str, Hospital],
        num_zips: int,
        max_packages_per_zip: int,
        zip_speed_mps: int,
        zip_max_cumulative_range_m: int,
    ):
        self.hospitals = hospitals
        self.num_zips = num_zips
        self.max_packages_per_zip = max_packages_per_zip
        self.zip_speed_mps = zip_speed_mps
        self.zip_max_cumulative_range_m = zip_max_cumulative_range_m

        # Track which orders haven't been launched yet
        self.unfulfilled_orders: List[Order] = []

    def queue_order(self, order: Order) -> None:
        """Add a new order to our queue.

        Note:
            Called every time a new order arrives.

        Args:
            order (Order): the order just placed.
        """

        self.unfulfilled_orders.append(order)

        # TODO: implement me!
        pass

    def launch_flights(self, current_time: int) -> List[Flight]:
        """Determines which flights should be launched right now.
        Each flight has an ordered list of Orders to serve.

        Note:
            Will be called periodically (approximately once a minute).

        Args:
            current_time (int): Seconds since midnight.

        Returns:
            list: Flight objects that launch at this time.

        Assumptions:
        - You may assume that the Zip flies a series of straight-line paths, starting at the Nest, passing through each hospital, and then returning to the Nest.
        - The total length of the cumulative path cannot be greater than the maximum range of the Zip (defined in the starter code).
        - Zips travel at a fixed flight speed (also defined in the starter code).
        - Zips can only take off with up to the maximum number of packages (also defined in the starter code).
        - Once they have returned, Zips charge instantly and can be immediately sent out again.
        - The Nest has a limited number of Zips (also defined in the starter code).
        """
        
        # SIMPLE NON-OPTOMIZED IMPLEMENTATION -- SINGLE TRIPS, HOSPITAL WITH MOST EMERGENCY ORDERS FIRST

        # check if there are any unfulfilled orders, if there aren't just return out
        if len(self.unfulfilled_orders) == 0: return []

        # create a dictionary of hospitals with key of the hospital and value of empty list
        resupply_hospitals_with_orders = { hospital:[] for hospital in self.hospitals.keys() }
        emergency_hospitals_with_orders = { hospital:[] for hospital in self.hospitals.keys() }

        # for each order in unfulfilled orders, add to respective hospital
        for order in self.unfulfilled_orders:
            if order.priority == EMERGENCY:
                emergency_hospitals_with_orders[order.hospital.name].append(order)
            else:
                resupply_hospitals_with_orders[order.hospital.name].append(order)
        
        # while there are still zip's available and there are still hospitals with unfulfilled orders
        flights = []
        while self.num_zips > 0 and (sum(
            [len(emergency_hospitals_with_orders[hospital]) for hospital in emergency_hospitals_with_orders]
            ) + sum(
            [len(resupply_hospitals_with_orders[hospital]) for hospital in resupply_hospitals_with_orders]
            )) > 0:

            # figure out which hospital has the most emergency orders
            target_hospital = None
            num_orders = 0
            for hospital in emergency_hospitals_with_orders:
                if len(emergency_hospitals_with_orders[hospital]) > num_orders:
                    target_hospital = emergency_hospitals_with_orders[hospital][0].hospital.name
                    num_orders = len(emergency_hospitals_with_orders[hospital])
            
            # if there were no emergency orders, select the hospital with the most resupply orders
            if target_hospital == None:
                for hospital in resupply_hospitals_with_orders:
                    if len(resupply_hospitals_with_orders[hospital]) > num_orders:
                        target_hospital = resupply_hospitals_with_orders[hospital][0].hospital.name
                        num_orders = len(resupply_hospitals_with_orders[hospital])

            # create a list of all orders we want to add to this flight, not capped
            all_orders_for_hospital = emergency_hospitals_with_orders[target_hospital]\
                                    + resupply_hospitals_with_orders[target_hospital]
            
            # figure out which orders we can accomedate on this flight
            orders_to_send = []
            for order in all_orders_for_hospital:
                if len(orders_to_send) <= MAX_PACKAGES_PER_ZIP:
                    orders_to_send.append(order)
                    
                    # remove the order from pending
                    if order in resupply_hospitals_with_orders[target_hospital]:
                        resupply_hospitals_with_orders[target_hospital].remove(order)
                    else:
                        emergency_hospitals_with_orders[target_hospital].remove(order)

                # zip is full, break and stage
                else: break
            
            # remove staged orders from the master queue
            for order in orders_to_send:
                self.unfulfilled_orders.remove(order)

            # assign the flight and decrement the number of available zips
            trip_time = get_trip_time_sec(
                start_x = 0,
                start_y = 0,
                end_x = orders_to_send[0].hospital.north_m,
                end_y = orders_to_send[0].hospital.east_m,
                speed = ZIP_SPEED_MPS
            )
            
            flights.append(Flight(
                    launch_time=current_time,
                    return_time=current_time + trip_time,
                    orders=orders_to_send
                )
            )
            self.num_zips -= 1

        if len(self.unfulfilled_orders) > 0:
            print(f'[{current_time}] there are unfulfilled orders and no zips left {self.unfulfilled_orders}')
        return flights


def find_point_on_line(start_x:int, start_y:int, end_x:int, end_y:int, speed:int, time:int, start_time:int):
    # calculate distance between start and end coordinates
    distance = math.sqrt((end_x - start_x)**2 + (end_y - start_y)**2)

    # calculate total time based on distance and speed
    total_time = distance / speed

    # calculate elapsed time based on start time and current time
    elapsed_time = time - start_time

    # calculate the ratio of elapsed time to total time
    time_ratio = elapsed_time / total_time

    # calculate the distance covered so far
    covered_distance = time_ratio * distance

    # interpolate the position between the start and end coordinates
    current_x = int(start_x + (end_x - start_x) * (covered_distance / distance))
    current_y = int(start_y + (end_y - start_y) * (covered_distance / distance))

    return current_x, current_y

def get_trip_time_sec(start_x:int, start_y:int, end_x:int, end_y:int, speed:int):
    # calculate distance between start and end coordinates
    distance = math.sqrt((end_x - start_x)**2 + (end_y - start_y)**2)

    # calculate total time based on distance and speed
    one_way_time = int(distance / speed)

    return one_way_time * 2

def point_angle_deg(start_x:int, start_y:int, end_x:int, end_y:int):
    dx = end_x - start_x
    dy = end_y - start_y
    
    angle_radians = math.atan2(dy, dx)
    angle_degrees = math.degrees(angle_radians)

    if angle_degrees < 0: angle_degrees += 360

    return int(angle_degrees)

class Runner:
    """
    A simulation runner that can playback order CSVs as if the day were
    progressing.
    """

    def __init__(self, hospitals_path: str, orders_path: str):
        with open(hospitals_path, "r") as f:
            self.hospitals = Hospital.load_from_csv(f)

        with open(orders_path, "r") as f:
            self.orders = Order.load_from_csv(f, self.hospitals)

        self.scheduler = ZipScheduler(
            hospitals=self.hospitals,
            num_zips=NUM_ZIPS,
            max_packages_per_zip=MAX_PACKAGES_PER_ZIP,
            zip_speed_mps=ZIP_SPEED_MPS,
            zip_max_cumulative_range_m=ZIP_MAX_CUMULATIVE_RANGE_M,
        )

        # create a place to track the active flights
        self.active_flights = []

    def run(self) -> None:
        """Run the simulator.
        This assumes any orders not fulfilled by the end of the day are failed.

        Note:
            This is a barebones implementation that should help get you
            started. You probably want to expand the runner's capabilities.
        """

        # Simulate time going from the first order time, until the end of the
        # day, in 1 minute increments
        sec_per_day = 24 * 60 * 60
        for sec_since_midnight in range(sec_per_day):
            # Find and queue pending orders.
            self.__queue_pending_orders(sec_since_midnight)
            self.__remove_returned_flights(sec_since_midnight)

            if sec_since_midnight % 60 == 0:

                # Once a minute, poke the flight launcher
                self.__update_launch_flights(sec_since_midnight)

                # Once a minute, log the simulation for visualizer
                flights = []
                for i in range(10):
                    try:
                        flight = self.active_flights[i]
                        flight_order = self.active_flights[i].orders[0]
                        
                        total_trip_time = get_trip_time_sec(
                            start_x=0,
                            start_y=0,
                            end_x=flight_order.hospital.east_m,
                            end_y=flight_order.hospital.north_m,
                            speed=ZIP_SPEED_MPS
                        )

                        # outbound
                        if sec_since_midnight < flight.launch_time + (total_trip_time / 2):
                            x, y = find_point_on_line(
                                start_x=0,
                                start_y=0,
                                end_x=flight_order.hospital.east_m,
                                end_y=flight_order.hospital.north_m,
                                speed=ZIP_SPEED_MPS,
                                time=sec_since_midnight,
                                start_time=flight.launch_time
                            )
                            angle = point_angle_deg(
                                start_x=0,
                                start_y=0,
                                end_x=flight_order.hospital.east_m,
                                end_y=flight_order.hospital.north_m,
                            )

                            flights.append({
                                'status': 'deployed',
                                'destination': flight_order.hospital.name,
                                'x': x,
                                'y': y,
                                'rotation': angle
                            })
                        
                        # inbound
                        else:
                            x, y = find_point_on_line(
                                start_x=flight_order.hospital.east_m,
                                start_y=flight_order.hospital.north_m,
                                end_x=0,
                                end_y=0,
                                speed=ZIP_SPEED_MPS,
                                time=sec_since_midnight,
                                start_time=flight.launch_time + (total_trip_time / 2)
                            )
                            angle = point_angle_deg(
                                start_x=flight_order.hospital.east_m,
                                start_y=flight_order.hospital.north_m,
                                end_x=0,
                                end_y=0,
                            )

                            flights.append({
                                'status': 'deployed',
                                'destination': 'Home',
                                'x': x,
                                'y': y,
                                'rotation': angle
                            })

                        #print(f"current time: {sec_since_midnight}")
                        #print(f"going to {flight_order.hospital.east_m}, {flight_order.hospital.north_m}")
                        #print(f"currently {x}, {y}")
                        #print(f"angle {angle}")
                        #print(f"return time: {flight.return_time}\n")

                    except IndexError:
                        flights.append({
                            'status': 'standby',
                            'destination': 'Home',
                            'x': 0,
                            'y': 0,
                            'rotation': 0
                        })

                open_orders = [
                    {
                        'time': order.time,
                        'destination': order.hospital.name,
                        'status': order.priority
                    }
                    for order in self.orders
                ]
                simulation_result[sec_since_midnight] = {'flights': flights,'futureOrders': open_orders}

        # These orders were not launched by midnight
        print(
            f"{len(self.scheduler.unfulfilled_orders)} unfulfilled orders at "
            + "the end of the day"
        )

    def __queue_pending_orders(self, sec_since_midnight: int) -> None:
        """Grab an order from the queue and queue it.

        Args:
            sec_since_midnight (int): Seconds since midnight.
        """
        while self.orders and self.orders[0].time == sec_since_midnight:
            # Find any orders that were placed during this second and tell
            # our scheduler about them
            order = self.orders.pop(0)
            print(
                f"[{sec_since_midnight}] {order.priority} order received",
                f"to {order.hospital.name}",
            )
            self.scheduler.queue_order(order)
            

    def __update_launch_flights(self, sec_since_midnight: int) -> None:
        """Schedule which flights should launch now.

        Args:
            sec_since_midnight (int): Seconds since midnight.
        """
        flights = self.scheduler.launch_flights(current_time=sec_since_midnight)
        if flights:
            print(f"[{sec_since_midnight}] Scheduling flights:")
            for f in flights: print(f)
        
        # save record of newly launched flights
        for flight in flights:
            self.active_flights.append(flight)


    def __remove_returned_flights(self, sec_since_midnight: int) -> None:
        """Remove returned flights from the register so that we can relaunch.

        Args:
            sec_since_midnight (int): Seconds since midnight.
        """
        flights_to_check = self.active_flights

        # Find any flights that have returned and ensure we inventory the zip
        for flight in flights_to_check:
            if flight.return_time <= sec_since_midnight:
                self.active_flights.remove(flight)

                print(f"[{sec_since_midnight}] {flight} returned to base")

                # track returned inventory
                self.scheduler.num_zips += 1


"""
Usage:

> python3 traveling_zip.py

Runs the provided CSVs
Feel free to edit this if you'd like
"""
if __name__ == "__main__":
    runner = Runner(
        hospitals_path='inputs/hospitals.csv',
        orders_path='inputs/orders.csv',
    )
    runner.run()

    # save the simulation
    with open('simulation.json', 'wt') as fio: json.dump(simulation_result, fio)
