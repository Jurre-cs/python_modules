if __name__ == "__main__":
    file_name = "new_discovery"
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n\n"
          f"Initializing new storage unit: {file_name}\n"
          "Storage unit created successfully...\n\n"
          "Inscribing preservation data...")
    try:
        with open(file_name, "w") as file:
            file.write("[ENTRY 001] New quantum algorithm discovered\n")
            file.write("[ENTRY 002] Efficiency increased by 347%\n")
            file.write("[ENTRY 003] Archived by Data Archivist trainee\n")
            file.close

        file = open(file_name)
        text = file.read()
        print(text)
        file.close()
        print("Data inscription complete. Storage unit sealed.")
        print(f"Archive '{file_name}' ready for long-term preservation.")

    except FileNotFoundError:
        print("File not found!!!")
