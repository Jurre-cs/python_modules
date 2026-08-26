
def secure_archive(filename, op, content=None):
    try:
        with open(filename, op) as file:
            if op == 'r':
                print("Using 'secure_archive' to read from a regular file:")
                print((True, file.read()))
            elif op == 'w':
                print("Using 'secure_archive' to write previous content \
to a new file:")
                file.write(content if content is not None else "")
                print("(True, 'Content successfully written to file')\n")
            else:
                print("Something done messed up\n")
    except FileNotFoundError:
        print("Using 'secure_archive' to read from a nonexistent file:")
        print(f'(False, "[Errno 2] No such file or directory: {filename}")\n')
    except PermissionError:
        print("Using 'secure_archive' to read from an inaccessible file:")
        print(f'(False, "[Errno 13] Permission denied: {filename}")\n')
    except Exception as e:
        print(f"(False, {e})")


if __name__ == "__main__":
    secure_archive("fileandnotsoshit.txt", "r")
    secure_archive("unaccessable.txt", "r")
    secure_archive("fileandshit.txt", "r")
    secure_archive("lifeandshit.txt", "w", "how dare UUUUU")
