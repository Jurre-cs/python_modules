class SecurePlant:
    def __init__(self, type, height, aged):
        self.type = type
        self.aged = aged
        self.height = height
        print(f"Plant Created: {self.type}")
    def set_height(self, new_height):
        if new_height > 0:
            self.height = self.height + new_height
            print(f"Height Updated: {self.height}")
        else:
            print("\nERROR, negative input!")
    def set_age(self, new_age):
        if new_age > 0:
            self.aged = self.aged + new_age
            print(f"Age Updated: {self.aged}")
        else:
            print("\nERROR, negative input!")
    def get_height(self):
        return(self.height)
    def get_age(self):
        return(self, aged)
    def get_info(self):
        print(f"Current plant Status: {self.type}, {self.height}, {self.aged}")

if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant1 = SecurePlant("rose", 21, 6)
    plant1.set_height(4)
    plant1.set_age(1)
    print()
    plant1.get_info()
