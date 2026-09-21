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
    except Exception as e:
        print(f"Error opening file '{filename}': {e}", file=sys.stderr)
        sys.exit(1)

    content: str = fragment.read()

    print("---")
    print(content, end="")
    print("---")

    fragment.close()
    print(f"File '{filename}' closed")

    print("Transform data:")
    lines = content.split("\n")
    transformed = [line + "#" for line in lines if line]

    print("---")
    for line in transformed:
        print(line)
    print("---")

    print("Enter new file name (or empty): ", end="")
    sys.stdout.flush()
    new_filename = sys.stdin.readline()
    new_filename = new_filename.strip()
    if new_filename == "":
        print("Not saving data")
    else:
        print(f"Saving data to '{new_filename}'")
        out: typing.IO = open(new_filename, "w")
        out.write("\n".join(transformed) + "\n")
        out.close()
        print(f"Data saved in file '{new_filename}'")
fragment: typing.IO = open(filename, "a")
