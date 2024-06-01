# enter your code here to solve the transporation assignment
# voer hier je code in om de vervoersvraag op te lossen
from abc import ABC, abstractmethod

class Passenger:

    @staticmethod
    def is_valid_name(name: str):
        return len(name.split()) >= 2
    
    def __init__(self, id: str, name: str, money: int) -> None:
        self.__name = ""
        self.id = id
        self.money = money
        self.name = name

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if not Passenger.is_valid_name(name):
            raise ValueError("invalid name")
        self.__name = name



class Vehicle(ABC):
    def __init__(self, license_plate: str, amount_of_seats: int) -> None:
        super().__init__()
        self.license_plate = license_plate
        self.amount_of_seats = amount_of_seats
        self.__occupants = {}

    @property
    def number_of_occupants(self):
        return len(self.__occupants)

    @abstractmethod
    def maximum_occupants(self):
        pass

    def add_passenger(self, passenger: Passenger):
        if passenger.id in self.__occupants:
            return
        if  self.number_of_occupants >= self.maximum_occupants:
            raise ValueError ("Vehicle full")
        
        self.__occupants[passenger.id] = passenger

    def remove_passenger(self, passenger_id: str):
        if passenger_id in self.__occupants:
            del self.__occupants[passenger_id]

    def remove_all_passagers(self):
        self.__occupants.clear()

    @property
    def occupant_name(self):
        return [occupant.name for occupant in self.__occupants.values()]

class Taxi(Vehicle):
    def __init__(self, license_plate: str, amount_of_seats: int) -> None:
        super().__init__(license_plate, amount_of_seats)
        self.is_available = True

    @property
    def maximum_occupants(self):
        return self.amount_of_seats
    
    def pickup(self, passengers: list[Passenger], distance: int):
        if not (self.is_available and self.number_of_occupants + len(passengers) <= self.maximum_occupants):
            raise ValueError("Go away")
        

        fare = 1 + distance
        if fare < 5:
            fare = 5

        if passengers[0].money < fare:
            raise RuntimeError("🦄")
        passengers[0].money -= fare

        for passenger in passengers:
            self.add_passenger(passenger)

        self.is_available = False

    def dropoff(self):
        pass

    
class Bus(Vehicle):
    def __init__(self, license_plate: str, amount_of_seats: int) -> None:
        super().__init__(license_plate, amount_of_seats)

    def maximum_occupants(self):
        return 2 * self.amount_of_seats
    
    def board(self, passenger):
        pass

    def disembark(self, passenger):
        pass

a = Passenger("1", "Nathan M", 15)
b = Passenger("2", "Andy A", 20)
c = Bus("a", 5)

"""
# enkele passagiers aanmaken
aimee = Passagier("12.34.56-789.01", "Aimee Backiel", 40)
bastian = Passagier("01.02.03-040.05", "Bastian Li Backiel", 5)

# enkele voertuigen aanmaken
mijn_taxi = Taxi("1-NGL-760", 4)
mijn_bus = Bus("1-HUE-344", 30)


# samen een busrit maken; Bastian betaalt graag zelf
mijn_bus.board(aimee)
mijn_bus.board(bastian)

# de inwoners van de bus controleren
mijn_bus.occupant_names
["Aimee Backiel", "Bastian Li Backiel"]

# ze stappen uit bij de dierentuin
mijn_bus.disembark(aimee)
mijn_bus.disembark(bastian)

# opnieuw de inwoners controleren
mijn_bus.occupant_names
[]

# Bastian wil voor het eerst alleen met de bus gaan en Aimee volgt hem in een taxi
# ze rijden slechts 5 km om zeker te zijn dat hij niet verdwaalt
mijn_bus.board(bastian)
mijn_taxi.pickup([aimee], 5)

# de inwoners in elk voertuig controleren
mijn_bus.occupant_names
["Bastian Li Backiel"]
mijn_taxi.occupant_names
["Aimee Backiel"]

# controleren hoeveel geld er nog over is in hun portemonnees
aimee.money
32
bastian.money
1
"""