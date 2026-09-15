class Plant:
    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float = 1.0) -> None:
        self._name: str = name
        self._height: float = 0.0
        self._age: int = 0
        self._growth_rate: float = growth_rate
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

    def grow(self) -> None:
        self.set_height(self._height + self._growth_rate)

    def age_one_day(self) -> None:
        self.set_age(self._age + 1)

    def show(self, prefix: str = "") -> None:
        print(f"{prefix}{self._name}: {round(self._height, 1)}cm, "
              f"{self._age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str,
                 growth_rate: float = 1.0) -> None:
        super().__init__(name, height, age, growth_rate)
        self._color: str = color
        self._blooming: bool = False

    def bloom(self) -> None:
        self._blooming = True

    def show(self, prefix: str = "") -> None:
        super().show(prefix)
        print(f"Color: {self._color}")
        if self._blooming:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float, growth_rate: float = 1.0) -> None:
        super().__init__(name, height, age, growth_rate)
        self._trunk_diameter: float = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of "
              f"{round(self._height, 1)}cm long and "
              f"{round(self._trunk_diameter, 1)}cm wide.")

    def show(self, prefix: str = "") -> None:
        super().show(prefix)
        print(f"Trunk diameter: {round(self._trunk_diameter, 1)}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, growth_rate: float = 1.0) -> None:
        super().__init__(name, height, age, growth_rate)
        self._harvest_season: str = harvest_season
        self._nutritional_value: float = 0.0

    def grow(self) -> None:
        super().grow()
        self._nutritional_value = self._nutritional_value + 0.5

    def age_one_day(self) -> None:
        super().age_one_day()
        self._nutritional_value = self._nutritional_value + 0.5

    def show(self, prefix: str = "") -> None:
        super().show(prefix)
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {round(self._nutritional_value)}")


def main() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April", 2.1)
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age_one_day()
    tomato.show()


if __name__ == "__main__":
    main()
