class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.buckets = [None] * self.size

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        if self.buckets[index] is None:
            self.buckets[index] = ListNode(key, value)
        else:
            current = self.buckets[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.size
        current = self.buckets[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return -1

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
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
