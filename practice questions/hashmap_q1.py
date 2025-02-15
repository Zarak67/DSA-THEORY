class HashMap:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        while self.table[index] is not None:
            index = (index + 1) % self.size
        self.table[index] = value

    def search(self, key):
        index = self.hash_function(key)
        while self.table[index] is not None:
            if self.table[index] == key:
                return index
            index = (index + 1) % self.size
        return None

hash_map = HashMap(10)
hash_map.insert(1, "one")
hash_map.insert(11, "eleven")
print("Value at key 1:", hash_map.search(1))
