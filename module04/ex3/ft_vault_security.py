
def secure_archive(filename: str, op: str,
                   content: str | None = None) -> tuple[bool, str | Exception]:
    try:
        with open(filename, op) as file:
            if op == 'r':
                print("Using 'secure_archive' to read from a regular file:")
                return ((True, file.read()))
            elif op == 'w':
                print("Using 'secure_archive' to write previous content \
to a new file:")
                file.write(content if content is not None else "")
                return (True, 'Content successfully written to file')
            else:
                return (False, "Something done messed up\n")
    except FileNotFoundError:
        print("Using 'secure_archive' to read from a nonexistent file:")
        return (False, f"[Errno 2] No such file or directory: '{filename}'")
    except PermissionError:
        print("Using 'secure_archive' to read from an inaccessible file:")
        return (False, f"[Errno 13] Permission denied: '{filename}'")
    except Exception as e:
        return (False, e)


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    print()
    print(secure_archive("fileandnotsoshit.txt", "r"))
    print()
    print(secure_archive("secure.txt", "r"))
    print()
    print(secure_archive("fileandshit.txt", "r"))
    print()
    print(secure_archive("lifeandshit.txt", "w", "how dare UUUUU"))
