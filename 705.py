class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.buckets = [None] * self.size

    def add(self, key: int) -> None:
        index = key % self.size
        if self.buckets[index] is None:
            self.buckets[index] = ListNode(key)
        else:
            current = self.buckets[index]
            while current:
                if current.key == key:
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = ListNode(key)

    def remove(self, key: int) -> None:
        index = key % self.size
        current = self.buckets[index]
        if not current:
            return
        if current.key == key:
            self.buckets[index] = current.next
            return
        prev = current
        current = current.next
        while current:
            if current.key == key:
                prev.next = current.next
                return
            prev = current
            current = current.next

    def contains(self, key: int) -> bool:
        index = key % self.size
        current = self.buckets[index]
        while current:
            if current.key == key:
                return True
            current = current.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
