class plant():
    def __init__(self, type, height, age):
        self.type = type
        self.height = height
        self.age = age
    def printing(self):
        print(self.type, self.height, self.age)

if __name__ == "__main__":
    plant1 = plant("rose", 23, 24)
    plant2 = plant("tulip", 21, 26)
    plant3 = plant("sunflower", 100, 48)
    print("=== garden xxxx registery ===")
    plant1.printing()
    plant2.printing()
    plant3.printing()