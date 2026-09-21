import random


def gen_event():
    names = ['bob', 'alice', 'charlie', 'dylan']
    actions = ['run', 'eat', 'sleep', 'grab', 'move', 'climb', 'swim', 'use',
               'release']

    while True:
        name = random.choice(names)
        action = random.choice(actions)
        yield (name, action)


def consume_event(events: list):
    while events:
        event = random.choice(events)
        events.remove(event)
        yield event


if __name__ == "__main__":
    event_stream = gen_event()
    for i in range(1000):
        name, action = next(event_stream)
        print(f"Event {i}: Player {name} did action {action}")

    ten_events = [next(event_stream) for _ in range(10)]
    print(f"Built list of 10 events: {ten_events}")

    for event in consume_event(ten_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events}")
