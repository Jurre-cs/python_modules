class Plant():
    def __init__(self, types, height, aged):
        self.types = types
        self.height = height
        self.aged = aged
    
class Flower(Plant):
    def __init__(self, types, height, aged, colour):
        super().__init__(types, height, aged)
        self.colour = colour
        print(f"{types} (Flower): {height}, {aged} days, {colour} colour")
    def bloom():
        print("Flower is blooming beautifully!")

class Tree(Plant):
    def __init__(self, types, height, aged, tree_diameter):
        super().__init__(types, height, aged)
        self.tree_diameter = tree_diameter
        print(f"{types} (Tree): {height}, {aged} days, {tree_diameter}cm diameter")
    def produce_shade(self):
        print(f"{self.types} provides {self.tree_diameter * self.height / 1000 * 3.14} square meters of shade")

class Vegetable(Plant):
    def __init__(self, types, height, aged, harvest_season, nutritional_value):
        super().__init__(types, height, aged)
        print(f"{types} (vegetable): {height}cm, {aged} days, {harvest_season} harvest")
        print(f"{types} is rich in {nutritional_value}")

if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    flower1 = Flower("lily", 80, 102, "pink")
    Flower.bloom()
    print()
    flower2 = Flower("sunflower", 123, 59, "yellow")
    Flower.bloom()
    print()
    tree1 = Tree("Birch", 480, 1234, 40)
    tree1.produce_shade()
    print()
    tree2 = Tree("spruce", 690, 1829, 60)
    tree2.produce_shade()
    print()
    Vegetable1 = Vegetable("iceberg lettuce", 30, 29, "spring/autumn", "no vitamines")
    print()
    Vegetable2 = Vegetable("spinach", 20, 37, "winter", "iron")
