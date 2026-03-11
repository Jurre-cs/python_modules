def water_plant(plant_list):
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    print("Opening watering system")
    for plant in plant_list:
        if plant == None:
            continue
        else:
            print(f"watering {plant}")
    print("Closing watering system (cleanup)")
    print("Watering completed successfully!\n")

def test_watering_system(plant_list):
    print("Testing with error...")
    print("Opening watering system")
    for plant in plant_list:
        try:
            if plant:
                print(f"watering {plant}")
            else:
                raise ValueError
        except ValueError:
            print("Error: Cannot water None - invalid plant!")
            break
    print("Closing watering system (cleanup)\n")
    print("Cleanup always happens, even with errors!")

if __name__ == "__main__":
    water_plant(["tomato", "lettuce", "watermelon", "carrots", "paprika", None])
    test_watering_system(["tomato", None, "lettuce", "watermelon", "carrots", "paprika", None])