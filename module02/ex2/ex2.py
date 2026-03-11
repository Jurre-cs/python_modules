class GardenError():
    def __init__(self, age, type, capacity):
        if age > 67:
            print(f"Caught PlantError: The {type} plant is wilting!")
        elif age < 0:
            print(f"Caught PlantError: Negative input! Not possible!")
        if capacity < 50:
            print("Caught Water: Not enough water in the tank!\n")
        elif capacity > 100:
            print("Caught WaterError: Tank if overflowing!\n")
        if -1 < age < 68 & 49 < capacity < 101:
            print("NO Error found\n")
        else:
            print("All custom error types work correctly!")
            
class WaterError(GardenError):
    def __init__(self, capacity):
        if capacity < 50:
            print("Caught Water: Not enough water in the tank!\n")
        elif capacity > 100:
            print("Caught WaterError: Tank if overflowing!\n")
        else:
            print("NO Error found")

class PlantError(GardenError):
    def __init__(self, age, type):
        if age > 67:
            print(f"Caught PlantError: The {type} plant is wilting!\n")
        elif age < 0:
            print(f"Caught PlantError: Negative input! Not possible!\n")
        else:
            print("NO Error found")
            
# minimum required capacity is 50L, maximum is 100
# plant older than 67 days is wilting

if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    plant = PlantError(70, "watermelon")
    print("Testing WaterError...")
    wateramount = WaterError(101)
    print("Testing catching all garden errors...")
    garden = GardenError(40, "koal", 74)