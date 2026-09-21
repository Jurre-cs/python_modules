import sys

if __name__ == "__main__":
    args_dict = {}
    print("=== Inventory System Analysis ===")

    if len(sys.argv) < 2:
        print("No items handed in!")
        sys.exit()
    for arg in sys.argv[1:]:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue
        key, value = arg.split(":", 1)
        if key in args_dict:
            print(f"Redundant item '{key}' - discarding")
            continue
        try:
            args_dict[key] = int(value)
        except ValueError as e:
            print(f"Quantity error for '{key}': {e}")

    print(f"Got inventory: {args_dict}")
    print(f"Item list: {list(args_dict.keys())}")

    total_quantity = sum(args_dict.values())
    print(f"Total quantity of the {len(args_dict)} items: {total_quantity}")

    for item, quantity in args_dict.items():
        percentage = (quantity / total_quantity) * 100
        print(f"Item {item} represents {percentage:.1f}%")

    most_abundant = max(args_dict, key=args_dict.__getitem__)
    least_abundant = min(args_dict, key=args_dict.__getitem__)
    print(f"Item most abundant: {most_abundant} with quantity \
{args_dict[most_abundant]}")
    print(f"Item least abundant: {least_abundant} with quantity \
{args_dict[least_abundant]}")

    args_dict['magic_item'] = 1
    print(f"Updated inventory: {args_dict}")
