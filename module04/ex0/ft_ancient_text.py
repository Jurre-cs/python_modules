import sys
import typing


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        sys.exit(1)

    filename = sys.argv[1]

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        fragment: typing.IO = open(filename, "r")
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
        sys.exit(1)

    print("---")
    print(fragment.read(), end="")
    print("---")

    fragment.close()
    print(f"File '{filename}' closed")
