class RandomizedSet(object):
    def __init__(self):
        self.lst = []
        self.idx_map = {}

    def search(self, val):
        return val in self.idx_map

    def insert(self, val):
        if self.search(val):
            return False

        self.lst.append(val)
        self.idx_map[val] = len(self.lst) - 1
        return True

    def remove(self, val):
        if not self.search(val):
            return False

        idx = self.idx_map[val]
        last_val = self.lst[-1]

        # Move the last element to the index of the element to delete
        self.lst[idx] = last_val
        self.idx_map[last_val] = idx

        # Remove the last element and delete from hashmap
        self.lst.pop()
        del self.idx_map[val]
        return True

    def getRandom(self):
        return random.choice(self.lst)
        


