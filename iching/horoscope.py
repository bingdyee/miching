
import numpy as np
from iching.hexagram import Hexagram, Trigram


_CHANGES =  [2, 3, 2, 3, 2, 3]

class Prophet:

    def __init__(self, seed = None):
        if seed is not None:
            np.random.seed(seed)

    def prophesy(self):
        """算卦"""
        changes = [np.random.choice(_CHANGES, size = 3).sum()  for i in range(6)]
        change_lines = [i + 1 for i, change in enumerate(changes) if change == 9 or change == 6]
        h = int(''.join([str(x % 2) for x in changes]), 2)
        hexagram = Trigram(h >> 3) + Trigram(h & 0x7)
        hexagram.change(change_lines)
        return changes, hexagram

    def explain(self):
        """解卦"""
        pass

    def visualize(self):
        """卦象可视化"""
        pass