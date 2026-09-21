def garden_operations(operation_number: int):
    if operation_number == 0:
        try:
            print("testing operation 0...")
            int("abc")
        except ValueError as Error:
            raise ValueError(f"Caught ValueError: {Error}")
    elif operation_number == 1:
        try:
            print("testing operation 1...")
            1 / 0
        except ZeroDivisionError as Error:
            raise ZeroDivisionError(f"Caught ZeroDivisionError: {Error}")
    elif operation_number == 2:
        try:
            print("testing operation 2...")
            open("/non/existent/file")
        except FileNotFoundError as Error:
            raise FileNotFoundError(f"Caught FileNotFoundError: {Error}")
    elif operation_number == 3:
        try:
            print("testing operation 3...")
            raise TypeError('can only concatenate str (not "int") to str')
        except TypeError as Error:
            raise TypeError(f"Caught TypeError: {Error}")
    else:
        print("testing operation 4...")
        print("Operation completed successfully\n")


def test_error_types():
    print("=== Garden Error Types Demo ===\n")
    for operation_number in range(5):
        try:
            garden_operations(operation_number)
        except (ValueError, ZeroDivisionError,
                FileNotFoundError, TypeError) as Error:
            print(Error)
    print("All error types tested successfully!\n")


if __name__ == "__main__":
    test_error_types()
