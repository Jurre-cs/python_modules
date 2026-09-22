from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import BattleStrategy, NormalStrategy
from ex2 import AggressiveStrategy, DefensiveStrategy


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    fighters = [(factory.create_base(), strategy)
                for factory, strategy in opponents]
    for index, (creature, strategy) in enumerate(fighters):
        for other, other_strategy in fighters[index + 1:]:
            print()
            print("* Battle *")
            print(creature.describe())
            print(" vs.")
            print(other.describe())
            print(" now fight!")
            try:
                strategy.act(creature)
                other_strategy.act(other)
            except ValueError as error:
                print(f"Battle error, aborting tournament: {error}")
                return


normal = NormalStrategy()
aggressive = AggressiveStrategy()
defensive = DefensiveStrategy()

print("Tournament 0 (basic)")
print(" [ (Flameling+Normal), (Healing+Defensive) ]")
battle([(FlameFactory(), normal), (HealingCreatureFactory(), defensive)])

print()
print("Tournament 1 (error)")
print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
battle([(FlameFactory(), aggressive), (HealingCreatureFactory(), defensive)])

print()
print("Tournament 2 (multiple)")
print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
battle([(AquaFactory(), normal),
        (HealingCreatureFactory(), defensive),
        (TransformCreatureFactory(), aggressive)])
