import math


def get_player_pos() -> tuple:
    coords = None
    index = 0
    while coords is None:
        coords = input("Enter new coordinates as floats in format 'x,y,z': ")
        try:
            if ',' not in coords or len(coords.split(',')) != 3:
                raise SyntaxError("Invalid syntax")
            for coord in coords.split(','):
                float(coord)
                index += 1
            return (tuple([float(x) for x in coords.split(',')]))
        except SyntaxError as e:
            print(e)
        except ValueError:
            print(f"Error on parameter '{coords.split(',')[index]}': \
could not convert to float: '{coords.split(',')[index]}'")
        coords = None
    return get_player_pos()


def use_player_pos():
    pos = get_player_pos()
    print(f"Got a first tuple: {pos}")
    print(f"it includes: X={pos[0]}, Y={pos[1]}, Z={pos[2]}")
    distance = math.sqrt(pos[0] ** 2 + pos[1] ** 2 + pos[2] ** 2)
    print(f"Distance to center: {round(distance, 4)}\n")


def main():
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    use_player_pos()
    print("Get a second set of coordinates")
    use_player_pos()


if __name__ == "__main__":
    main()
