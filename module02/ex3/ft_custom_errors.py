class PlantError(Exception):
    def __init__(self, age: int, plant_type: str):
        try:
            if age > 67:
                raise Exception(f"Caught PlantError: \
The {plant_type} plant is wilting!\n")
            elif age < 0:
                raise Exception("Caught PlantError: \
Negative input! Not possible!\n")
        except Exception as e:
            print(e)


class WaterError(Exception):
    def __init__(self, capacity: int):
        try:
            if capacity > 100:
                raise Exception("Caught WaterError: \
The water capacity is too high!\n")
            elif capacity < 0:
                raise Exception("Caught WaterError: \
Not enough water in the tank!!\n")
        except Exception as e:
            print(e)


class GardenError(Exception):
    def __init__(self, age: int, plant_type: str, capacity: int):
        try:
            if age > 67:
                raise Exception(f"Caught GardenError: \
The {plant_type} plant is wilting!")
            elif age < 0:
                raise Exception("Caught GardenError: \
Negative input! Not possible!")
        except Exception as e:
            print(e)
        try:
            if capacity > 100:
                raise Exception("Caught GardenError: \
The water capacity is too high!\n")
            elif capacity < 10:
                raise Exception("Caught GardenError: \
Not enough water in the tank!!\n")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    plant = PlantError(70, "watermelon")

    print("Testing WaterError...")
    wateramount = WaterError(-1)

    print("Testing GardenError...")
    garden = GardenError(70, "tomato", 2)
    print("All custom error types work correctly!")
