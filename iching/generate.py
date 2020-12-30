# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw


# Year = 1983
Heavenly = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
Earthly = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
Symbolic = ['鼠', '牛', '虎', '兔', '龙', '蛇', '马', '羊', '猴', '鸡', '狗', '猪']

# [
#     '甲子', '乙丑', '丙寅', '丁卯', '戊辰', '己巳', '庚午', '辛未', '壬申', '癸酉',
#     '甲戌', '乙亥', '丙子', '丁丑', '戊寅', '己卯', '庚辰', '辛巳', '壬午', '癸未',
#     '甲申', '乙酉', '丙戌', '丁亥', '戊子', '己丑', '庚寅', '辛卯', '壬辰', '癸巳',
#     '甲午', '乙未', '丙申', '丁酉', '戊戌', '己亥', '庚子', '辛丑', '壬寅', '癸卯',
#     '甲辰', '乙巳', '丙午', '丁未', '戊申', '己酉', '庚戌', '辛亥', '壬子', '癸丑', 
#     '甲寅', '乙卯', '丙辰', '丁巳', '戊午', '己未', '庚申', '辛酉', '壬戌', '癸亥'
# ]

def jiazi_chronology(year):
    n = year - 3
    return Heavenly[n % 10 - 1] + Earthly[n % 12 - 1], Symbolic[n % 12 - 1]


def jiazi_table():
    HE = []
    i = j = 0
    while True:
        he = Heavenly[i] + Earthly[j]
        if he in HE:
            break
        HE.append(he)
        i = 0 if i == 9 else i + 1
        j = 0 if j == 11 else j + 1
    return HE


# (NO, Lower trigram, Upper trigram)
Hexagrams = [
    (1, 7, 7), (2, 0, 0), (3, 4, 2), (4, 2, 1), 
    (5, 7, 2), (6, 2, 7), (7, 2, 0), (8, 0, 2), 
    (9, 7, 3), (10, 6, 7), (11, 7, 0), (12, 0, 7),
    (13, 5, 7), (14, 7, 5), (15, 1, 0), (16, 0, 4),
    (17, 4, 6), (18, 3, 1), (19, 6, 0), (20, 0, 3),
    (21, 4, 5), (22, 5, 1), (23, 0, 1), (24, 4, 0),
    (25, 4, 7), (26, 7, 1), (27, 4, 1), (28, 3, 6),
    (29, 2, 2), (30, 5, 5), (31, 1, 6), (32, 3, 4),
    (33, 1, 7), (34, 7, 4), (35, 0, 5), (36, 5, 0),
    (37, 5, 3), (38, 6, 5), (39, 1, 2), (40, 2, 4),
    (41, 6, 1), (42, 4, 3), (43, 7, 6), (44, 3, 7),
    (45, 0, 6), (46, 3, 0), (47, 2, 6), (48, 3, 2),
    (49, 5, 6), (50, 3, 5), (51, 4, 4), (52, 1, 1),
    (53, 1, 3), (54, 6, 4), (55, 5, 4), (56, 1, 5),
    (57, 3, 3), (58, 6, 6), (59, 2, 3), (60, 6, 2),
    (61, 6, 3), (62, 1, 4), (63, 5, 2), (64, 2, 5)
]

# 天道左旋，地道右旋
# 乾一、兑二、离三、震四、巽五、坎六、艮七、坤八
# 1-Yang 0-Yin
# Lift -> Right = Bottom -> Top (Yao)
# Trigrams_cn = { '乾': '111', '兑': '110', '离': '101', '震': '100', '巽': '011', '坎': '010', '艮': '001', '坤': '000'}
# Trigrams_en = ['Earth', 'Mountain', 'Water', 'Wind', 'Thunder', 'Fire', 'Lake', 'Heaven']

# 7-乾、兑-6、离-5、震-4、巽-3、坎-2、艮-1、坤-0
Trigrams = ['坤', '艮', '坎', '巽', '震', '离', '兑', '乾']
trigram = lambda t: '{:03b}'.format(t if isinstance(t, int) else Trigrams.index(t))


def yang(draw, xy, yang_w, h, color = 0):
    x, y = xy[0], xy[1]
    draw.rectangle((x, y, x + yang_w, y + h), fill = color)


def yin(draw, xy, yin_w, h, color = 0):
    x, y = xy[0], xy[1]
    draw.rectangle((x, y, x + yin_w, y + h), fill = color)
    draw.rectangle((x + yin_w + h, y, x + yin_w * 2 + h , y + h), fill = color)


def iching_hexagram(gua, size = (110, 110), yang_c = 0, yin_c = 0):
    yang_w, h = size[0], size[1] / 11
    yin_w = (yang_w - h) / 2
    x, y = 0, size[1] - h
    im = Image.new('RGB', size, 'white')
    draw = ImageDraw.Draw(im)
    # First Yao -> Sixth Yao
    for ch in gua:
        if ch == '0':
            yin(draw, (x, y), yin_w, h, color = yin_c)
        elif ch == '1':
            yang(draw, (x, y), yang_w, h, color = yang_c)
        else:
            continue
        y -= 2 * h
    return im


def show_hexagram():
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['font.family']='sans-serif'
    plt.figure(figsize = (13, 13))
    for hexagram in Hexagrams:
        plt.subplot(8, 8, hexagram[0])
        lower_trigram = trigram(hexagram[1])
        upper_trigram = trigram(hexagram[2])
        plt.imshow(iching_hexagram(lower_trigram + upper_trigram, yang_c = 'red', yin_c = 'blue'))
        plt.axis('off')
        plt.title('{}.{}上{}下'.format(hexagram[0], Trigrams[hexagram[2]], Trigrams[hexagram[1]]))
    plt.tight_layout()
    plt.show()


def iching_hexagram_test(gua = '010101'):
    plt.figure()
    plt.imshow(iching_hexagram(gua, yang_c = 'red', yin_c = 'blue'))
    plt.axis('equal')
    plt.axis('off')
    plt.tight_layout()
    plt.show()




if __name__ == '__main__':
    show_hexagram()
    # iching_hexagram_test()

