def input_temperature(temp_int: int):
    print(f"input data is '{temp_int}'")
    try:
        temp_int = int(temp_int)
        print(f"Temperature is now {temp_int}°C\n")
    except ValueError as Error:
        raise ValueError(f"{Error}\n")


def test_temperature():
    print("=== Garden Temperature ===\n")
    for temp_str in ["25", "abc"]:
        try:
            input_temperature(temp_str)
        except ValueError as Error:
            print(f"Caught input_temperature error: {Error}")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
