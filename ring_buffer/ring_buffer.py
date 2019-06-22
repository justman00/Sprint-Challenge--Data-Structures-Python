class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        # current should be the oldest element in the list
        # append will put the item in the storage at the current index

        # check if the current is equal to capacity and reset it to be 0
        if self.current == self.capacity:
            self.current = 0

        self.storage[self.current] = item
        self.current += 1

    def get(self):
        return list(filter(lambda x: x != None, self.storage))
