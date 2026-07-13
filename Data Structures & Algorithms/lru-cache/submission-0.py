class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashSet = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.hashSet:
            return -1
        self.hashSet.move_to_end(key)
        return self.hashSet[key] 

    def put(self, key: int, value: int) -> None:
        if key in self.hashSet:
            self.hashSet.move_to_end(key)
        self.hashSet[key] = value

        if len(self.hashSet) > self.capacity:
            self.hashSet.popitem(last = False)
        
