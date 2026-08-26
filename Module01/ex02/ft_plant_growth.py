class plant():
    def __init__(self, type, height, aged):
        self.type = type
        self.height = height
        self.aged = aged
    def printing(self):
        print(self.type, self.height, self.aged)
    def get_info(self):
        return(self.type, self.height, self.aged)
    def grow(self):
        self.height = self.height + 1
    def age(self):
        self.aged = self.aged + 1

if __name__ == "__main__":
    plant1 = plant("roos", 20, 13)
    print("=== Day 1 ===")
    plant1.printing()
    for i in range(6):
        plant1.age()
        plant1.grow()
    print("=== Day 7 ===")
    plant1.printing()
    print(f"growth this week: +{i + 1}")