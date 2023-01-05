class Hamburger:
    def __init__(self, ingredients):
        self.ingredients = ingredients
    #static methods do not need an object to work
    #static methods are different from class methods because they do not have the implicit first argument cls
    @staticmethod
    def rightIngredient(ingredients):
        if ingredients == "ice cream":
            raise ValueError("Ew, what is that???")
        else:
            return True
yum = ["bun", "cheese", "burger", "ketchup", "mustard", "lettuce", "tomato", "ice cream"]
if all(Hamburger.rightIngredient(i) for i in yum):
    hum = Hamburger(yum)
print(hum.ingredients)