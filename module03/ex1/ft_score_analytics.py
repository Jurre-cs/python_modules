import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    args = sys.argv
    if len(args) < 2:
        print("No scores provided. Usage: python3 \
ft_score_analytics.py <score1> <score2> ...")
    else:
        safe = True
        unsafe = []
        for x in args[1:]:
            if not x.isdigit():
                print(f"Invalid parameter: '{x}'")
                safe = False
                unsafe.append(x)
        if unsafe == args[1:]:
            print("No scores provided. Usage: python3 \
ft_score_analytics.py <score1> <score2> ...")
            sys.exit(1)
        elif not safe:
            print("Some scores are invalid. \
Please provide only numeric scores.")
            sys.exit(1)
        numbers = [int(x) for x in args[1:]]
        total = 0
        print(f"Scores processed: [{', '.join(args[1:])}]")
        print(f"Total players: {len(args) - 1}")
        print(f"Total score: {sum(numbers)}")
        print(f"Average score: {sum(numbers) / (len(args) - 1)}")
        print(f"High score: {max(numbers)}")
        print(f"Low score: {min(numbers)}")
        if len(numbers) > 1:
            print(f"Score range: {max(numbers) - min(numbers)}")
        else:
            print(f"Score range: {numbers[0]}")
