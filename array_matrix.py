class CustomArray:
    def __init__(self):
        self.data = []

    def insert(self, index, value):
        self.data.insert(index, value)

    def delete(self, index):
        return self.data.pop(index)

    def access(self, index):
        return self.data[index]
