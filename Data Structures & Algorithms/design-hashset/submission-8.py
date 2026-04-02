class MyHashSet:

    def __init__(self):
        self.n_buckets = 1000
        self.buckets = [[] for i in range(self.n_buckets)]

    def add(self, key: int) -> None:
        bucket = self.buckets[key % self.n_buckets]
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        bucket = self.buckets[key % self.n_buckets]
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        bucket = self.buckets[key % self.n_buckets]
        return key in bucket

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)