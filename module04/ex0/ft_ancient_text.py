if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print("Accessing Storage Vault: ancient_fragment.txt")
    print("Connection established...\n")

    try:
        file = open("ancient_fragment.txt", "r")
        print("RECOVERED DATA:")
        text = file.read()
        print(text)
        print("\nData recovery complete. Storage unit disconnected.")
        file.close()
    except FileNotFoundError:
        print("file not found")
