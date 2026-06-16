class GardenManager():
    def __init__(self, plant_list, plant_name, water_level, sunlight_hours):
        self.plant_list = plant_list
        self.plant_name = plant_name
        self.water_level = water_level
        self. sunlight_hours = sunlight_hours

    def water_plant(self,plant_list):
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

    def check_plant_health(self):
        if plant_name == "":
            raise ValueError("Plant name cannot be empty!\n")
        if water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)\n")
        if water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 1)\n")
        if sunlight_hours > 12:
            raise ValueError(f"Sunlight hours {sunlight_hours} is too high (max 12)\n")
        if sunlight_hours < 2:
            raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)\n")
        print(f"Plant '{plant_name}' is healthy!\n")

    def add_plant(self):
        self.plant_list.append(plant_name)