def check_temperature(temp_str):
	print(f"Testing temperature: {temp_str}")
	try:
		temp_str = int(temp_str)
		if temp_str >= 0 & temp_str <= 40:
			print(f"Temperature {temp_str}°C is perfect for plants!\n")
		elif temp_str > 40:
			print(f"Error: {temp_str}°C is too hot for plants (max 40°C)\n")
		else:
			print(f"Error: {temp_str} is too cold for plants (min 0°C)\n")
	except ValueError:
		print(f"'{temp_str}' is not a valid number\n")
	print("All tests completed - program didn't crash!")

def test_temperature_input():
	print("=== Garden Temperature Checker ===\n")
	check_temperature("25")
	check_temperature("abc")
	check_temperature("100")
	check_temperature("-50")

test_temperature_input()