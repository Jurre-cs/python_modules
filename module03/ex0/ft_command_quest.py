import sys

if __name__ == "__main__":
    args = sys.argv
    amount = 1
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if len(args) < 2:
        print("No arguments provided!")
        print("Total arguments: 1")
    else:
        print(f"Arguments received: {len(args) - 1}")
        for arg in args[1:]:  # Skip the program name
            print(f"Argument {amount}: {arg}")
            amount += 1
        print(f"Total arguments: {len(args)}")
