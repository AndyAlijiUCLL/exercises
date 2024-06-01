# enter your code here to solve the housing assignment
# voer hier je code in om de huisvestingsvraag op te lossen
from abc import ABC, abstractmethod


class Person:

    @staticmethod
    def is_valid_name(name):
        return len(name.split()) >= 2

    def __init__(self, is_a_student, name: str, id: str ) -> None:
        self.id = id
        self.name = name
        self.is_a_student = is_a_student
    

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
         if not self.is_valid_name(name):
            return ValueError("invalid name")
         self.__name = name




class Residence(ABC):
    def __init__(self, address: str , area: float, number_of_rooms: int) -> None:
        super().__init__()
        self.address = address
        self.area = area
        self.number_of_rooms = number_of_rooms
        self.__occupants =  {} # or dict()

    @property
    def number_of_occupants(self):
        return len(self.__occupants)
    
    @property
    def maximum_occupants(self):
        #return min(self.area // 20, self.number_of_rooms * 2)
        mopa = self.area // 20
        mopr = self.number_of_rooms * 2
        return min(mopa, mopr)

    def register_resident(self, person):
       """ if person.id not in self.__occupants:
            if self.number_of_occupants < self.maximum_occupants:
                self.__occupants[person.id] = person
            else:
                raise RuntimeError("Not enough room for another resident")"""
       if person.id in self.__occupants:
           return
       
       if self.number_of_occupants >= self.maximum_occupants:
                raise RuntimeError("not enough")
       
       self.__occupants[person.id] = person

    

    def unregister_resident(self, id):
        if id in self.__occupants:
            del self.__occupants[id]

    @property
    def resident_names(self):
        return [resident.name for resident in self.__occupants.values()]
    
    @abstractmethod
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
    

aimee = Person("12.34.56-789.01","Aimee Backiel",False)
bastian = Person("01.02.03-040.05", "Bastian Li Backiel", True)

my_villa = Villa("Roeselbergdal 44, 3012 Wilsele", 151, 4, 1)
print(my_villa.calculate_value())
print(my_villa.maximum_occupants)