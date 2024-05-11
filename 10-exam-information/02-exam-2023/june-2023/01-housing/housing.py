# enter your code here to solve the housing assignment
# voer hier je code in om de huisvestingsvraag op te lossen
from abc import ABC, abstractmethod


class Persoon:
    def __init__(self, is_a_student, name: str, id: str ) -> None:
        if not self.is_valid_name(name):
            return ValueError("invalid name")
        self.id = id
        self.__name = name
        self.is_a_student = is_a_student

    @staticmethod
    def is_valid_name(name):
        s = name.split()
        return len(name) >= 2
    

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not self.is_valid_name(value):
            raise ValueError('invalid name')
        self.__name = value

class Residence(ABC):
    def __init__(self, address: str , area: float, number_of_rooms: int) -> None:
        super().__init__()
        self.address = address
        self.area = area
        self.number_of_rooms = number_of_rooms
        self.__occupants = {}

    @property
    def number_of_occupants(self):
        return len(self.__occupants)
    
    @property
    @abstractmethod
    def maximum_occupants(self):
        pass

    def register_resident(self, person):
        pass

    def unregister_resident(self, id):
        if id in self.__occupants:
            del self.__occupants[id]

    @property
    def resident_names(self):
        return [resident.name for resident in self.__occupants.values()]

    def calculate_value(self):
        pass

class Villa(Residence):
    def __init__(self, address: str, area: float, number_of_rooms: int, garage_capacity: int) -> None:
        super().__init__(address, area, number_of_rooms)
        self.garage_capacity = garage_capacity

    def calculate_value(self):
        return (25000 * self.number_of_rooms) + (2100 * self.area) + (10000 * self.garage_capacity)

class StudentKot(Residence):
    def __init__(self, address: str, area: float) -> None:
        super().__init__(address, area)

    def register_resident(self, person):
        if not person.is_a_student:
            raise RuntimeError("Only students can register in a StudentKot")
        super().register_resident(person)
    
    def calculate_value(self):
        return 150000 + (750 * self.area)