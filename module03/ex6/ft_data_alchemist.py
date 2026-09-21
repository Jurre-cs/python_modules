import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    players: list[str] = ["Alice", "bob", "Charlie", "dylan", "Emma",
                          "Gregory", "john", "kevin", "Liam",]
    print(f"Initial list of players: {players}")

    all_caps: list[str] = [n.capitalize() for n in players]
    print(f"New list with all names capitalized: {all_caps}")

    caps_only: list[str] = [n for n in players if n == n.capitalize()]
    print(f"New list of capitalized names only: {caps_only}")

    scores: dict[str, int] = {n: random.randint(0, 1000) for n in all_caps}
    print(f"Score dict: {scores}")

    average: float = sum(scores.values()) / len(scores)
    print(f"Score average is {round(average, 2)}")

    high_scores: dict[str, int] = {
        n: s for n, s in scores.items() if s > average}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
