import random
class Vague:
    #initial object creation
    def __init__(self, cheese):
        self.cheese = cheese
    #random length given between 0 and 2 times the real length
    def __len__(self):
        return random.randint(0,len(self.cheese)*2)
    #random index given within 2 from wanted value
    def __getitem__(self, indie):
        return self.cheese[indie + random.randint(-2,2)]
vague = Vague(["Aligator", "Boar", "Crocodile", "Dog", "Elephant", "Fox", "Gorilla", "Horse", "Iguana"])
print(len(vague))
print(len(vague))
print(vague[2])
print(vague[2])