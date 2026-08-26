import random


def gen_player_achievements():
    print("=== Achievement Tracker System ===")

    # Pool of possible achievements to randomly distribute from
    achievement_pool = [
        'Crafting Genius', 'World Savior', 'Master Explorer',
        'Collector Supreme', 'Untouchable', 'Boss Slayer', 'Strategist',
        'level_10', 'treasure_hunter', 'speed_demon', 'perfectionist',
        'Speed Runner', 'Unstoppable'
    ]

    players = ['alice', 'bob', 'charlie', 'dylan']

    def random_achievements(pool, min_count=3, max_count=7):
        count = random.randint(min_count, max_count)
        return set(random.sample(pool, count))

    achievements = {player: random_achievements(achievement_pool) for player
                    in players}

    alice = achievements['alice']
    bob = achievements['bob']
    charlie = achievements['charlie']
    dylan = achievements['dylan']

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")
    print(f"Player dylan achievements: {dylan}\n")

    all_achievements = alice.union(bob, charlie, alice, dylan)
    print(f"All distinct achievements: {all_achievements}\n")

    allhavethis = alice.intersection(bob, charlie, dylan)
    print(f"Common Achievements: {allhavethis}\n")

    print(f"Alice unique: {alice.difference(bob, charlie, dylan)}")
    print(f"Bob unique: {bob.difference(alice, charlie, dylan)}")
    print(f"Charlie unique: {charlie.difference(alice, bob, dylan)}")
    print(f"Dylan unique: {dylan.difference(alice, bob, charlie)}\n")

    print("Alice is missing:", all_achievements.difference(alice))
    print("Bob is missing:", all_achievements.difference(bob))
    print("Charlie is missing:", all_achievements.difference(charlie))
    print("Dylan is missing:", all_achievements.difference(dylan))


if __name__ == "__main__":
    gen_player_achievements()
