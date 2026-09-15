class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name: str = name
        self._height: float = 0.0
        self._age: int = 0
        self.set_height(height)
        self.set_age(age)

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            return False
        self._height = height
        return True

    def set_age(self, age: int) -> bool:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            return False
        self._age = age
        return True

    def show(self, prefix: str = "") -> None:
        print(f"{prefix}{self._name}: {round(self._height, 1)}cm, "
              f"{self._age} days old")


def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    rose.show("Plant created: ")
    print()

    new_height: float = 25.0
    if rose.set_height(new_height):
        print(f"Height updated: {round(new_height)}cm")

    new_age: int = 30
    if rose.set_age(new_age):
        print(f"Age updated: {new_age} days\n")

    if not rose.set_height(-5.0):
        print("Height update rejected")

    if not rose.set_age(-3):
        print("Age update rejected\n")

    rose.show("Current state: ")


if __name__ == "__main__":
    main()
