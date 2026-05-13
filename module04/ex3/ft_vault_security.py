if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    with open("classified_data.txt", 'r') as file:
        print("Vault connection established with failsafe protocols")
        print("SECURE EXTRACTION:")
        file.read()
    print("\nSECURE PRESERVATION:")
    with open("security_protocols.txt", 'w') as file:
        file.write("added stuff")
        print("[CLASSIFIED] New security protocols archived")
    print("Vault automatically sealed upon completion\n")
    print("All vault operations completed with maximum security.")