# prophesy horoscopes
import numpy as np
from hexagram import Hexagram, Trigram
from pickles.chings import iching_txt, horoscopes



_CHANGES =  [2, 3, 2, 3, 2, 3]

class Prophet:

    def prophesy(self):
        yaos = [np.random.choice(_CHANGES, size = 3).sum()  for i in range(6)]
        change_lines = []
        changes = []
        for i, change in enumerate(yaos):
            if change == 6:
                changes.append('老阴')
                change_lines.append(i + 1)
            if change == 7:
                changes.append('少阳')
            if change == 8:
                changes.append('少阴')
            if change == 9:
                changes.append('老阳')
                change_lines.append(i + 1)
        h = int(''.join([str(x % 2) for x in yaos]), 2)
        hexagram = Trigram(h >> 3) + Trigram(h & 0x7)
        hexagram.change(change_lines)
        return changes, hexagram


if __name__ == '__main__':
    prophet = Prophet()
    changes, hexagram,  = prophet.prophesy()
    print('\n************************ 算卦 ************************\n')
    print('起卦：', changes, hexagram)
    print('本卦：', hexagram.details(0))
    if hexagram.is_changed():
        print('\n************************ 变卦：{}爻变 ************************\n'.format(hexagram.change_lines))
        print('变卦：', hexagram.details(1))
        gua_2 = iching_txt[hexagram.changed]
    print('\n************************ 解卦 ************************\n')
    gua_1 = iching_txt[hexagram.changes]
    change_len = len(hexagram.change_lines)
    if change_len == 0:
        gua_ci = gua_1[3]
        print('本卦-卦辞：{}'.format(gua_ci))
    if change_len == 1 or change_len == 2:
        for ch_idx in hexagram.change_lines:
            ch_idx -= 1
            print('变卦-卦爻：', gua_2[4][ch_idx])
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
