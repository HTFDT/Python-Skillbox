from typing import Tuple


class Transport:
    def __init__(self, coordinates: Tuple[float, float], speed: float, brand: str, year: int, number: int, *args,
                 **kwargs):
        self.coordinates = coordinates
        self.speed = speed
        self.brand = brand
        self.year = year
        self.number = number

    @property
    def coordinates(self):
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, value):
        self.__coordinates = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        self.__speed = value

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        self.__brand = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value

    def __str__(self):
        property_names = [p for p in dir(type(self)) if isinstance(getattr(type(self), p), property)]
        return (f"{self.__class__.__name__}: "
                f"{{ {', '.join([f'{p}: {getattr(self, p)}' for p in property_names])} }}")

    def is_in_area(self, pos_x: float, pos_y: float, length: float, width: float) -> bool:
        return pos_x <= self.coordinates[0] <= pos_x + length and pos_y <= self.coordinates[1] <= pos_y + width


class Passenger:
    @property
    def passengers_capacity(self):
        return self.__passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        self.__passengers_capacity = passengers_capacity

    @property
    def number_of_passengers(self):
        return self.__number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        self.__number_of_passengers = number_of_passengers


class Cargo:
    @property
    def carrying(self):
        return self.__carrying

    @carrying.setter
    def carrying(self, carrying):
        self.__carrying = carrying


class Plane(Transport):
    def __init__(self, coordinates: Tuple[float, float], speed: float, brand: str, year: int, number: int,
                 height: float, *args, **kwargs):
        super().__init__(coordinates, speed, brand, year, number, *args, **kwargs)
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        self.__height = val


class Auto(Transport):
    def __init__(self, coordinates: Tuple[float, float], speed: float, brand: str, year: int, number: int,
                 weight: float, *args, **kwargs):
        super().__init__(coordinates, speed, brand, year, number, *args, **kwargs)
        self.weight = weight

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, val):
        self.__weight = val


class Ship(Transport):
    def __init__(self, coordinates: Tuple[float, float], speed: float, brand: str, year: int, number: int, port: str,
                 *args, **kwargs):
        super().__init__(coordinates, speed, brand, year, number, *args, **kwargs)
        self.port = port

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, value):
        self.__port = value


class Car(Auto):
    def __init__(self, coordinates: Tuple[float, float], speed: float, brand: str, year: int, number: int,
                 weight: float, has_child_seat: bool, *args, **kwargs):
        super().__init__(coordinates, speed, brand, year, number, weight, *args, **kwargs)
        self.has_child_seat = has_child_seat

    @property
    def has_child_seat(self):
        return self.__has_child_seat

    @has_child_seat.setter
    def has_child_seat(self, value):
        self.__has_child_seat = value


class Bus(Auto, Passenger):
    def __init__(self, coordinates: Tuple[float, float], speed: float, brand: str, year: int, number: int,
                 weight: float, number_of_passengers: int, passengers_capacity: int, *args, **kwargs):
        super().__init__(coordinates, speed, brand, year, number, weight, *args, **kwargs)
        self.number_of_passengers = number_of_passengers
        self.passengers_capacity = passengers_capacity


class CargoAuto(Auto, Cargo):
    def __init__(self, coordinates: Tuple[float, float], speed: float, brand: str, year: int, number: int,
                 weight: float, carrying, *args, **kwargs):
        super().__init__(coordinates, speed, brand, year, number, weight, *args, **kwargs)
        self.carrying = carrying


class Boat(Ship):
    def __init__(self, coordinates: Tuple[float, float], speed: float, brand: str, year: int, number: int, port: str,
                 *args, **kwargs):
        super().__init__(coordinates, speed, brand, year, number, port, *args, **kwargs)


class PassengerShip(Ship, Passenger):
    def __init__(self, coordinates: Tuple[float, float], speed: float, brand: str, year: int, number: int, port: str,
                 number_of_passengers: int, passengers_capacity: int, *args, **kwargs):
        super().__init__(coordinates, speed, brand, year, number, port, *args, **kwargs)
        self.number_of_passengers = number_of_passengers
        self.passengers_capacity = passengers_capacity


class CargoShip(Ship, Cargo):
    def __init__(self, coordinates: Tuple[float, float], speed: float, brand: str, year: int, number: int, port: str,
                 carrying, *args, **kwargs):
        super().__init__(coordinates, speed, brand, year, number, port, *args, **kwargs)
        self.carrying = carrying


class SimplePlane(Plane):
    def __init__(self, coordinates: Tuple[float, float], speed: float, brand: str, year: int, number: int,
                 height: float, *args, **kwargs):
        super().__init__(coordinates, speed, brand, year, number, height, *args, **kwargs)


class PassengerPlane(Plane, Passenger):
    def __init__(self, coordinates: Tuple[float, float], speed: float, brand: str, year: int, number: int,
                 height: float, number_of_passengers: int, passengers_capacity: int, *args, **kwargs):
        super().__init__(coordinates, speed, brand, year, number, height, *args, **kwargs)
        self.number_of_passengers = number_of_passengers
        self.passengers_capacity = passengers_capacity


class CargoPlane(Plane, Cargo):
    def __init__(self, coordinates: Tuple[float, float], speed: float, brand: str, year: int, number: int,
                 height: float, carrying, *args, **kwargs):
        super().__init__(coordinates, speed, brand, year, number, height, *args, **kwargs)
        self.carrying = carrying


class SeaPlane(Plane, Ship):
    def __init__(self, coordinates: Tuple[float, float], speed: float, brand: str, year: int, number: int,
                 height: float, port: str, *args, **kwargs):
        super().__init__(coordinates, speed, brand, year, number, height=height, port=port, *args, **kwargs)
