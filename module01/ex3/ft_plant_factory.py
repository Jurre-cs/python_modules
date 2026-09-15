class Plant:
    def __init__(self, name: str, height: float, age_days: int,
                 growth_rate: float = 1.0) -> None:
        self.name: str = name
        self.height: float = height
        self.age_days: int = age_days
        self.growth_rate: float = growth_rate

    def grow(self) -> None:
        self.height = self.height + self.growth_rate

    def age(self) -> None:
        self.age_days = self.age_days + 1

    def show(self, prefix: str = "") -> None:
        print(f"{prefix}{self.name}: {round(self.height, 1)}cm, "
              f"{self.age_days} days old")


def main() -> None:
    garden: list[Plant] = [
        Plant("Rose", 25.0, 30, 0.8),
        Plant("Oak", 200.0, 365, 0.2),
        Plant("Cactus", 5.0, 90, 0.05),
        Plant("Sunflower", 80.0, 45, 3.0),
        Plant("Fern", 15.0, 120, 0.4),
    ]

    print("=== Plant Factory Output ===")
    for plant in garden:
        plant.show("Created: ")


if __name__ == "__main__":
    main()
