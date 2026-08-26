def input_temperature(temp_str):
    print(f"input data is '{temp_str}'")
    try:
        temp_str = int(temp_str)
    except ValueError as Error:
        raise ValueError(f"{Error}\n")
    if temp_str > 40:
        raise ValueError(f": {temp_str}°C is too hot for plants (max 40°C)\n")
    if temp_str < 0:
        raise ValueError(f": {temp_str}°C is too cold for plants (min 0°C)\n")
    else:
        print(f"Temperature is now {temp_str}°C\n")


def test_temperature():
    print("=== Garden Temperature ===\n")
    for temp_str in ["25", "abc", "100", "-50"]:
        try:
            input_temperature(temp_str)
        except ValueError as Error:
            print(f"Caught input_temperature error: {Error}")
    print("All tests completed - program didn't crash!")


# if __name__ == "__main__":
#     test_temperature()
