from mammal import Mammal


class DomesticAnimal(Mammal):
    def __init__(self, ID, species, name, size, weight, owner, noise, diet):
        self.ID = ID
        self.species = species
        self.name = name
        self.size = size
        self.weight = weight
        self.owner = owner
        self.noise = noise
        self.diet = diet


    def __str__(self):
        return f'ID = {self.ID} \nSpecies = {self.species} \nName = {self.name} \nSize = {self.size}m ' \
               f'\nWeight = {self.weight}kg \nOwner = {self.owner} \nNoise = {self.noise} \nDiet = {self.diet} \n '


def main():
    domestic_animal1 = DomesticAnimal(6, "Dog", "Goldie", 0.7, 25, "John", "BARK!", "Dog food")
    domestic_animal2 = DomesticAnimal(5, "cat", "Garfield", 0.5, 15, "Jonathan", "meow", "Lasagna")


main()
