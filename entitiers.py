class Animal:
    """Animal """
    def __init__(self, legs, eyes, hair_color) -> None:
        self.legs = legs
        self.eyes = eyes
        self.hair_color = hair_color

class Terrestrial:
    planet = 'Tierra'

class Human(Animal, Terrestrial):
    def __init__(self, hair_color, eye_color) -> None:
        super().__init__(2,2,hair_color)
        self.eye_color = eye_color
    def get_planet(self):
        return self.planet


class Spider(Animal):
    def __init__(self,hair_color) -> None:
        super().__init__(8, 8, hair_color)

# class Person(Human): 
#     hair_color = 'cafe'
#     eye_color = 'cafe'

human = Human('Negro', 'azul')
#print(human.get_planet()) #Multi-herencia



