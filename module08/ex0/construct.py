
import os
import site
import sys


def in_virtual_env() -> bool:
    return sys.prefix != sys.base_prefix


def outside_matrix() -> None:
    print("MATRIX STATUS: You're still plugged in")
    print()
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate  # On Windows")
    print()
    print("Then run this program again.")


def inside_construct() -> None:
    env_path = sys.prefix
    env_name = os.path.basename(env_path)
    print("MATRIX STATUS: Welcome to the construct")
    print()
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {env_name}")
    print(f"Environment Path: {env_path}")
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print()
    print("Package installation path:")
    print(site.getsitepackages()[0])


def main() -> None:

    if in_virtual_env():
        inside_construct()
    else:
        outside_matrix()


if __name__ == "__main__":
    main()
