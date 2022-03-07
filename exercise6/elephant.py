from mammal import Mammal


class Elephant(Mammal):
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
    my_elephant = Elephant(8, "elephant", "Dumbo", 1.5, 100, "Helen Aberson", "trumpeting", "Herbivore")
    print(my_elephant.__str__())


main()
