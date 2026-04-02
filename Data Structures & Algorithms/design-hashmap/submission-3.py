class MyHashMap:

    def __init__(self):
        self.n_buckets = 100
        self.buckets = [[] for i in range(self.n_buckets)]

    def put(self, key: int, value: int) -> None:
        for i, kv in enumerate(self.buckets[key % self.n_buckets]):
            if key == kv[0]:
                self.buckets[key % self.n_buckets][i] = (key, value)
                return
        self.buckets[key % self.n_buckets].append((key, value))

    def get(self, key: int) -> int:
        for k, v in self.buckets[key % self.n_buckets]:
            if key == k:
                return v
        return -1

    def remove(self, key: int) -> None:
        value = self.get(key)
        try:
            self.buckets[key % self.n_buckets].remove((key, value))
        except:
            pass


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)