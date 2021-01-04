# Visualizing the prophesy process.

from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
from hexagram import _HEXAGRAM, _TRIGRAMS


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
    for i in range(6):
        n = (gua >> (5 - i)) & 1
        if n == 0:
            yin(draw, (x, y), yin_w, h, color = yin_c)
        if n == 1:
            yang(draw, (x, y), yang_w, h, color = yang_c)
        y -= 2 * h
    return im


def show_hexagram():
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['font.family']='sans-serif'
    plt.figure(figsize = (13, 13))
    for i, hexagram in enumerate(_HEXAGRAM):
        plt.subplot(8, 8, i + 1)
        lower = hexagram >> 3
        upper = hexagram & 0x7
        plt.imshow(iching_hexagram(hexagram, yang_c = 'red', yin_c = 'blue'))
        plt.axis('off')
        plt.title('{}.{}上{}下'.format(i + 1, _TRIGRAMS[upper], _TRIGRAMS[lower]))
    plt.tight_layout()
    plt.show()


def iching_hexagram_test(gua = 0):
    plt.figure()
    plt.imshow(iching_hexagram(gua, yang_c = 'red', yin_c = 'blue'))
    plt.axis('equal')
    plt.axis('off')
    plt.tight_layout()
    plt.show()
