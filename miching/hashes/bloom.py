from .mmh3 import hash


class BloomFilter:
    """
    simple boolm filter
    """

    def __init__(self, size = 1 << 25):
        self.bits = 0
        self.size = size

    def add(self, val):
        self.bits |= (1 << self.hash(val))

    def hash(self, val):
        return hash(val) & (self.size - 1)

    def lookup(self, val):
        h = self.hash(val)
        return self.bits >> h & 1 == 1

    def restore(self, bits):
        self.bits = bits