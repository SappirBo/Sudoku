class table:
    def __init__(self, start_number: int):
        self.mat = []
        for i in range(0, 3):
            self.mat.append([start_number, start_number, start_number])

    def print_table(self):
        for i in self.mat:
            print(i)