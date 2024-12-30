class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return self.size() < 1

    def push(self, item):
        if not self.full():
            return self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        return self.items[self.size()-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return self.size() >= self.limit

    def search(self, target):
        try:
            target_index = self.items.index(target)
            end = self.size()-1
            #print(target_index,end, end - target_index)
            return end - target_index
        except ValueError:
            return -1
