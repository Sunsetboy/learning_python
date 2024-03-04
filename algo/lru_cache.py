from collections import OrderedDict

class LruCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = OrderedDict()

    def get(self, key):
        if key in self.dict:
            self.dict.move_to_end(key)
            return self.dict[key]
        return -1

    def set(self, key, value):
        if key in self.dict:
            self.dict.move_to_end(key)
        self.dict[key] = value

        if len(self.dict) > self.capacity:
            self.dict.popitem(last=False)

if __name__ == "__main__":
    cache = LruCache(2)
    cache.set("a", 1)
    cache.set("b", 2)
    cache.get("a")
    cache.set("c", 3)
    print(f"cache: {cache.dict}")
    cache.set("a", 3)
    cache.get("b")
