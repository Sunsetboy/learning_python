class Iter:

    def __init__(self, step):
        self.counter = 0
        self.step = step

    def __next__(self):
        self.counter += self.step
        return self.counter
    

if __name__ == "__main__":
    iter = Iter(3)

    while True:
        curr_element = next(iter)
        print(curr_element)
        if curr_element > 100:
            break
