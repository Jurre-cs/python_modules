from typing import Generator
import random
import time

def game_events(n) -> Generator | tuple[int, int, int]:
	Treasure_events = 0
	Level_up_events = 0
	High_level_players = 0
	player1 = random.randint(1, 100)
	player2 = random.randint(1, 100)
	player3 = random.randint(1, 100)
	player4 = random.randint(1, 100)
	players = {"henk":player1, "bob":player2, "charles":player3, "ben":player4}
	for event in range(n):
		rand_event = random.randint(1, 3)
		key, value = random.choice(list(players.items()))
		if value > 9:
			High_level_players += 1
		if rand_event < 2:
			yield (f"Event {event}: Player {key} (level {value}) killed a monster")
		elif rand_event < 3:
			Treasure_events += 1
			yield (f"Event {event}: Player {key} (level {value}) found treasure")
		elif rand_event < 4:
			Level_up_events += 1
			yield (f"Event {event}: Player {key} (level {value + 1}) leveled up")
	return Treasure_events, Level_up_events, High_level_players

def main() -> None:
	start = time.perf_counter()
	print("=== Game Data Stream Processor ===\n")
	print("Processing 1000 game events...\n")

	Total_events = 0
	n = random.randint(1, 1000)
	for present in game_events(n):
		Total_events += 1
		print(present)
	Treasure_events, Level_up_events, High_level_players = game_events(0)
	print("\n=== Stream Analytics ===")
	print(f"Total events processed: {Total_events}")
	print(f"High-level players (10+): {High_level_players}")
	print(f"Treasure events: {Treasure_events}")
	print(f"Level-up events: {Level_up_events}")
	print("Memory usage: Constant (streaming)")
	end = time.perf_counter()
	print(f"Processing time: {end - start:.6f} seconds\n")
	print("=== Generator Demonstration ===")

if __name__ == "__main__":
	main()