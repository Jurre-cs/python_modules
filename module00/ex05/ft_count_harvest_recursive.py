def ft_count_harvest_recursive(Days = None, i = 0):
    if Days is None:
        Days = int(input("Days until harvest: "))
    if i == Days:
        print("Harvest time!")
        return
    print(f"Day {i + 1}")
    ft_count_harvest_recursive(Days, i + 1)

ft_count_harvest_recursive()