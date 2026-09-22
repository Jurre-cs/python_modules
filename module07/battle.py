from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    for creature in (factory.create_base(), factory.create_evolved()):
        print(creature.describe())
        print(creature.attack())


def battle(first: CreatureFactory, second: CreatureFactory) -> None:
    print("Testing battle")
    challenger = first.create_base()
    defender = second.create_base()
    print(challenger.describe())
    print(" vs.")
    print(defender.describe())
    print(" fight!")
    print(challenger.attack())
    print(defender.attack())


flame = FlameFactory()
aqua = AquaFactory()

test_factory(flame)
print()
test_factory(aqua)
print()
battle(flame, aqua)
