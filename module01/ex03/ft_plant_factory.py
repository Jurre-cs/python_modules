class plant():
    i = 0
    def __init__(self, type, height, age):
        self.type = type
        self.height = height
        self.age = age
        plant.i += 1
    def printing(self):
        print(f"Created: {self.type}, {self.height}, {self.age}")
    def print_num():
        print(f"Total plants created: {plant.i}")

if __name__ == "__main__":
    plant("roos", 23, 4).printing()
    plant("tulip", 21, 67).printing()
    plant("watermelon", 79, 129).printing()
    plant("birch", 700, 3502).printing()
    plant("potato", 10, 42).printing()
    plant.print_num()
