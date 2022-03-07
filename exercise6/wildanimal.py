from mammal import Mammal


class WildAnimal(Mammal):
    def __init__(self, ID, species, name, size, weight, noise, diet, color):
        self.ID = ID
        self.species = species
        self.name = name
        self.size = size
        self.weight = weight
        self.noise = noise
        self.diet = diet
        self.color = color


    def __str__(self):
        return f'ID = {self.ID} \nSpecies = {self.species} \nName = {self.name} \nSize = {self.size}m ' \
               f'\nWeight = {self.weight}kg \nNoise = {self.noise} \nDiet = {self.diet} \nColor = {self.color} \n '


def main():
    animal1 = WildAnimal(8, "Bear", "Unknown", 2, 200, "ROAR!", "Fish, grasses, roots, berries", "Brown")
    animal2 = WildAnimal(9, "Hog", "Unknown", 1, 100, "oink!", "Plants", "Black / Gray")





main()
