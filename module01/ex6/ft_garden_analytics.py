class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0

        def count_grow(self) -> None:
            self._grow_calls = self._grow_calls + 1

        def count_age(self) -> None:
            self._age_calls = self._age_calls + 1

        def count_show(self) -> None:
            self._show_calls = self._show_calls + 1

        def display(self) -> None:
            print(f"Stats: {self._grow_calls} grow, "
                  f"{self._age_calls} age, "
                  f"{self._show_calls} show")

    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float = 1.0) -> None:
        self._name: str = name
        self._height: float = 0.0
        self._age: int = 0
        self._growth_rate: float = growth_rate
        self._stats: Plant.Stats = self.Stats()
        self.set_height(height)
        self.set_age(age)

    @staticmethod
    def is_older_than_a_year(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

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

    def grow(self, days: int = 1) -> None:
        self.set_height(self._height + self._growth_rate * days)
        self._stats.count_grow()

    def age(self, days: int = 1) -> None:
        self.set_age(self._age + days)
        self._stats.count_age()

    def show(self, prefix: str = "") -> None:
        print(f"{prefix}{self._name}: {round(self._height, 1)}cm, "
              f"{self._age} days old")
        self._stats.count_show()

    def show_stats(self) -> None:
        self._stats.display()


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 color: str = "unknown", growth_rate: float = 1.0) -> None:
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


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int,
                 color: str = "unknown", seed_potential: int = 0,
                 growth_rate: float = 1.0) -> None:
        super().__init__(name, height, age, color, growth_rate)
        self._seed_potential: int = seed_potential
        self._seed_count: int = 0

    def bloom(self) -> None:
        super().bloom()
        self._seed_count = self._seed_potential

    def show(self, prefix: str = "") -> None:
        super().show(prefix)
        print(f"Seeds: {self._seed_count}")


class Tree(Plant):
    class Stats(Plant.Stats):

        def __init__(self) -> None:
            super().__init__()
            self._shade_calls: int = 0

        def count_shade(self) -> None:
            self._shade_calls = self._shade_calls + 1

        def display(self) -> None:
            super().display()
            print(f"{self._shade_calls} shade")

    _stats: "Tree.Stats"

    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float = 0.0,
                 growth_rate: float = 1.0) -> None:
        super().__init__(name, height, age, growth_rate)
        self._trunk_diameter: float = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of "
              f"{round(self._height, 1)}cm long and "
              f"{round(self._trunk_diameter, 1)}cm wide.")
        self._stats.count_shade()

    def show(self, prefix: str = "") -> None:
        super().show(prefix)
        print(f"Trunk diameter: {round(self._trunk_diameter, 1)}cm")


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.get_name()}]")
    plant.show_stats()


def main() -> None:
    print("=== Garden statistics ===")

    print("=== Check year-old")
    for days in (30, 400):
        answer = Plant.is_older_than_a_year(days)
        print(f"Is {days} days more than a year? -> {answer}")
    print()

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red", 8.0)
    rose.show()
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_statistics(rose)
    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)
    print()
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow", 42, 30.0)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_statistics(sunflower)
    print()
    print("=== Anonymous")
    nobody = Plant.anonymous()
    nobody.show()
    display_statistics(nobody)


if __name__ == "__main__":
    main()
