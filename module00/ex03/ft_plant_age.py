def ft_plant_age():
    plant_age = input("Enter plant age in days: ")
    plant_age = int(plant_age)
    if plant_age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
ft_plant_age()