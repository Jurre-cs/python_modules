def water_plant(plant_name):
    try:
        if plant_name[0].islower():
            raise Exception(f"Caught PlantError: \
The {plant_name} plant is wilting!")
        else:
            print(f"Watering {plant_name} [OK]")
    except Exception as e:
        print(e)
        return False
    return True


def test_watering_system():
    print("=== Garden Watering System ===\n")
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        for plant in ["Tomato", "Lettuce", "Carrot"]:
            value = water_plant(plant)
            if value is False:
                print(".. ending tests and returning to main")
                break
    except Exception as e:
        print(e)
    finally:
        print("Closing watering system\n")
    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        for plant in ["Tomato", "lettuce", "Carrot"]:
            value = water_plant(plant)
            if value is False:
                print(".. ending tests and returning to main")
                break
    except Exception as e:
        print(e)
    finally:
        print("Closing watering system\n")
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
