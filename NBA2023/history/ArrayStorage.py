class ArrayStorage:
    def __init__(self):
        self.array = []

    def add_element(self, element):
        self.array.append(element)

    def get_element(self, index):
        if 0 <= index < len(self.array):
            return self.array[index]
        else:
            raise IndexError("Index out of range")

    def get_size(self):
        return len(self.array)

    def print_array(self):
        print(self.array)
