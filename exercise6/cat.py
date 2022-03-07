from mammal import Mammal


class Cat(Mammal):
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
               f'\nWeight = {self.weight}kg \nOwner = {self.owner} \nNoise = {self.noise} \nDiet = {self.diet} '


def main():
    my_cat = Cat(5, "cat", "Garfield", 0.5, 15, "Jonathan", "meow", "Lasagna")
    print(my_cat.__str__())


main()



