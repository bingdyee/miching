import argparse
import numpy as np
from hexagram import Hexagram, Trigram
from pickles.chings import iching_txt, horoscopes
from version import __version__

_CHANGES =  [2, 3, 2, 3, 2, 3]

class Prophet:

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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "Any vital question you may have, ask it here.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-q', dest= 'question', help = "the question you are going to ask for")
    group.add_argument('-t', dest= 'topic', help = "the topic about your question")
    parser.add_argument('-s', dest = 'seed', type=int, help = "the random seed (not recommended)")
    parser.add_argument('-v', dest = 'visual', type=bool, default = False, help = "visualizing the prophesy process")
    parser.add_argument('-o', dest = 'output', help = "write to file instead of stdout")
    parser.add_argument('-V', '--version', action = 'version', version = __version__, help = "show this version message and exit")
    args = parser.parse_args()
    if args.seed:
        np.random.seed(args.seed)

    # TODO question classification
    # [情感、决策、事业、运势]
    prophet = Prophet()
    _, hexagram,  = prophet.prophesy()
    print('\n************************ 算卦 ************************\n')
    print('起卦：', hexagram)
    print('本卦：', hexagram.details(0))
    if hexagram.is_changed():
        print('\n************************ 变卦：{}爻变 ************************\n'.format(hexagram.change_lines))
        print('变卦：', hexagram.details(1))
        gua_2 = iching_txt[hexagram.changed]
    print('\n************************ 解卦 ************************\n')
    gua_1 = iching_txt[hexagram.changes]
    change_len = len(hexagram.change_lines)
    if change_len == 0:
        print('本卦-卦辞：', gua_1[3])
    if change_len == 1 or change_len == 2:
        for ch_idx in hexagram.change_lines:
            ch_idx -= 1
            print('本卦-爻辞：', gua_1[4][ch_idx])
    if change_len == 3:
        print('本卦-卦辞：', gua_1[3])
        print('变卦-卦辞：', gua_2[3])
    if change_len == 4 or len == 5:
        ch_idxs = set([i for i in range(1, 7)]).difference(hexagram.change_lines)
        for ch_idx in ch_idxs:
            ch_idx -= 1
            print('变卦-爻辞：', gua_2[4][ch_idx])
    if change_len == 6:
        print('变卦-卦辞：', gua_2[3])
    print()
    print('\n'.join(horoscopes[hexagram.changes]))
