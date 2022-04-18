class Zoo:
    __animals = 0
    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        output = ""
        if species == "mammal":
            output += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            output += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif species == "bird":
            output += f"Birds in {self.name}: {', '.join(self.birds)}\n"

        output += f"Total animals: {Zoo.__animals}"
        return output


zoo_name = input()
zoo = Zoo(zoo_name)

number = int(input())
for i in range(number):
    animal = input().split(" ")
    species = animal[0]
    name = animal[1]
    zoo.add_animal(species, name)

species_info = input()
print(zoo.get_info(species_info))
