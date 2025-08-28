import random
from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        self.list = []
        self.dict = defaultdict(set)

    def insert(self, val: int) -> bool:
        self.dict[val].add(len(self.list))
        self.list.append(val)
        return len(self.dict[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.dict[val]:
            return False
        idx = self.dict[val].pop()
        last_idx = len(self.list) - 1
        last_val = self.list[last_idx]
        if idx != last_idx:
            self.list[idx] = last_val
            self.dict[last_val].remove(last_idx)
            self.dict[last_val].add(idx)
        self.list.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
