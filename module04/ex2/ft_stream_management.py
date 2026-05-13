import sys

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    Id = input("Input Stream active. Enter archivist ID: ")
    print("Input Stream active. Enter status report: ", end="")
    sys.stdout.flush()
    Status = sys.stdin.readline()
    sys.stdout.write(f"\n[STANDARD] Archive status from {Id}: {Status}")
    sys.stdout.flush()
    print("[ALERT] System diagnostic: Communication channels verified",
          file=sys.stderr)
    sys.stdout.write("[STANDARD] Data transmission complete\n\n")
    print("Three-channel communication test successful.")
