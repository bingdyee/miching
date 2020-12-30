# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw


# 天道左旋，地道右旋
# 乾一、兑二、离三、震四、巽五、坎六、艮七、坤八
# 1-Yang 0-Yin
# Lift -> Right = Bottom -> Top (Yao)
Bagua = { '111': 'Qian', '110': 'Dui', '101': 'Li', '100': 'Zhen', '011': 'Xun', '010': 'Kan', '001': 'Gen', '000': 'Kun'}


def yang(draw, xy, yang_w, h, color = 0):
    x, y = xy[0], xy[1]
    draw.rectangle((x, y, x + yang_w, y + h), fill = color)

def yin(draw, xy, yin_w, h, color = 0):
    x, y = xy[0], xy[1]
    draw.rectangle((x, y, x + yin_w, y + h), fill = color)
    draw.rectangle((x + yin_w + h, y, x + yin_w * 2 + h , y + h), fill = color)
    
def hexagram(gua, size = (110, 110), yang_c = 0, yin_c = 0):
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


if __name__ == '__main__':
    plt.figure()
    plt.imshow(hexagram('000101'))
    plt.axis('equal')
    plt.axis('off')
    plt.tight_layout()
    plt.show()
