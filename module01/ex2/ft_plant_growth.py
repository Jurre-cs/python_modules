
class Plant:
    def __init__(self, name: str, height: float, age_days: int,
                 growth_rate: float) -> None:
        self.name: str = name
        self.height: float = height
        self.age_days: int = age_days
        self.growth_rate: float = growth_rate

    def grow(self) -> None:
        self.height = self.height + self.growth_rate

    def age(self) -> None:
        self.age_days = self.age_days + 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, "
              f"{self.age_days} days old")


def main() -> None:
    rose = Plant("Rose", 25.0, 30, 0.8)
    start_height: float = rose.height
    print("=== Garden Plant Growth ===")
    rose.show()

    for day in range(1, 8):
        rose.grow()
        rose.age()
        print(f"=== Day {day} ===")
        rose.show()

    print(f"Growth this week: {round(rose.height - start_height, 1)}cm")


if __name__ == "__main__":
    main()
