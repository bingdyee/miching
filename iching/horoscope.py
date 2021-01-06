
import numpy as np
from iching.hexagram import Hexagram, Trigram
from iching.visualize import show_hexagram
from iching.datasets.chings import iching_txt, horoscopes

_CHANGES =  [2, 3, 2, 3, 2, 3]

class Prophet:

    def __init__(self, event = None, seed = None):
        self.event = event
        if seed is not None:
            np.random.seed(seed)
        

    def prophesy(self):
        """算卦"""
        print('\n************************ 算卦 ************************\n')
        changes = [np.random.choice(_CHANGES, size = 3).sum()  for i in range(6)]
        change_lines = [i + 1 for i, change in enumerate(changes) if change == 9 or change == 6]
        h = int(''.join([str(x % 2) for x in changes]), 2)
        hexagram = Trigram(h >> 3) + Trigram(h & 0x7)
        hexagram.change(change_lines)
        self.cur_hexagram = hexagram
        self.cur_changes = changes
        print('起卦：', hexagram)
        print('本卦：', hexagram.details(0))
        return changes, hexagram

    def explain(self, hexagram = None):
        """解卦"""
        target = hexagram if hexagram is not None else self.cur_hexagram
        if target is None:
            print('无卦可解。。。')
            return
        print('\n************************ 解卦 ************************\n')
        gua_1 = iching_txt[target.changes]
        if target.is_changed():
            print('\n************************ 变卦：{}爻变 ************************\n'.format(target.change_lines))
            print('变卦：', target.details(1))
            gua_2 = iching_txt[target.changed]
            change_len = len(target.change_lines)
            if change_len == 1 or change_len == 2:
                for ch_idx in target.change_lines:
                    ch_idx -= 1
                    print('本卦-爻辞：', gua_1[4][ch_idx])
            if change_len == 3:
                print('本卦-卦辞：', gua_1[3])
                print('变卦-卦辞：', gua_2[3])
            if change_len == 4 or len == 5:
                ch_idxs = set([i for i in range(1, 7)]).difference(target.change_lines)
                for ch_idx in ch_idxs:
                    ch_idx -= 1
                    print('变卦-爻辞：', gua_2[4][ch_idx])
            if change_len == 6:
                print('变卦-卦辞：', gua_2[3])
        else:
            print('本卦-卦辞：', gua_1[3])
        print()
        print('\n'.join(horoscopes[target.changes]))
        

    def visualize(self):
        """卦象可视化"""
        show_hexagram(self.cur_hexagram.changes)

    def print(self, info):
        print(info)