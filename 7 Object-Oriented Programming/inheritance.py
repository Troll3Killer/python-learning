class Planet:
    round = True
    def __init__(self, name, mass, distance):
        self.name = name
        self.mass = mass
        self.distance = distance
#InnerPlanet and OuterPlanet inherit methods from Planet
class InnerPlanet(Planet):
    rocky = True
    gassy = False
class OuterPlanet(Planet):
    rocky = False
    gassy = True
Mercury = InnerPlanet("Mercury", 0.055, 0.4)
Venus = InnerPlanet("Venus", 0.815, 0.7)
Earth = InnerPlanet("Earth", 1, 1)
Mars = InnerPlanet("Mars", 0.11, 1.5)
Jupiter = OuterPlanet("Jupiter", 318, 5.2)
Saturn = OuterPlanet("Saturn", 95, 9.5)
Uranus = OuterPlanet("Uranus", 14.5, 19.8)
Neptune = OuterPlanet("Neptune", 17, 30)
print(Mars.gassy)
print(Mars.mass)
print(Saturn.gassy)
print(Neptune.name)