import sys
import math

def mathing(position):
	for n in position:
		n = float(n)
	distance = math.sqrt((position[0] - 0.0)**2 + (position[1] - 0.0)**2 + (position[2] - 0.0)**2)
	distance = "%.2f" % distance
	return distance

if __name__ == "__main__":
	print("=== Game Coordinate System ===\n")
	position = sys.argv
	if len(sys.argv) != 4:
		x, y, z = 3, 4, 0
	else:
		x, y, z = position[1:]
	cords = (10, 20, 5)
	errorexample = ("abc", "def", "ghi")
	print(f"Position created:  {cords}")

	try:
		for num1 in cords:
			num1 = int(num1)
		print(f"Distance between (0, 0, 0) and {cords}: {mathing(cords)}\n")
	except ValueError:
		print(f"could not convert {num1} to float\n")

	try:
		print(f"Parsing coordinates: \"{x},{y},{z}\"")
		position = (float(x), float(y), float(z))
		print(f"Parsed position: ({x}, {y}, {z})")
		print(f"Distance between (0, 0, 0) and ({x}, {y}, {z}): {mathing(position)}")
	except ValueError:
		print(f"Parsing invalid coordinates: {position}\n")

	try:
		errorexample = tuple(errorexample)
	except ValueError:
		print(f'Parsing invalid coordinates: "{errorexample}"')
	try:
		for num3 in errorexample:
			num3 = int(num3)
	except ValueError:
		print(f"Error parsing coordinates: invalid literal for int() with base 10: '{num3}'")
		print(f"Error details - Type: ValueError, Args: (\"invalid literal for int() with base 10: '{num3}'\",)\n")

	print("Unpacking demonstration:") 
	print(f"Player at x={x}, y={y}, z={z}")
	print(f"Coordinates X={x}, Y={y}, Z={z}")
