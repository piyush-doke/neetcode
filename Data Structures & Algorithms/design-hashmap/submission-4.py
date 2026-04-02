class MyHashMap:

    def __init__(self):
        self.n_buckets = 100
        self.buckets = [[] for _ in range(self.n_buckets)]

    def put(self, key: int, value: int) -> None:
        idx = key % self.n_buckets
        bucket = self.buckets[idx]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    def get(self, key: int) -> int:
        idx = key % self.n_buckets

        for k, v in self.buckets[idx]:
            if k == key:
                return v

        return -1

    def remove(self, key: int) -> None:
        idx = key % self.n_buckets
        bucket = self.buckets[idx]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return
