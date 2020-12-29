# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection


def broken_line(xy, w, h, spacing):
    x, y = xy[0], xy[1]
    w = (w - spacing) / 2
    return [mpatches.Rectangle(xy, w, h), mpatches.Rectangle((x + w + spacing, y), w, h)]

def line(xy, w, h):
    return [mpatches.Rectangle(xy, w, h)]

def qian(xy = (0, 1.), w = 1.1, h = .1, spacing = 0.1):
    """
    Qian(Heaven)
    """
    patches = []
    x, y = xy[0], xy[1]
    patches += line(xy, w, h)
    patches += line((x, y - spacing - h), w, h)
    patches += line((x, y - 2 * (spacing + h)), w, h)
    return patches

def dui(xy = (0, 1.), w = 1.1, h = .1, spacing = 0.1):
    """
    Dui(Lake)
    """
    patches = []
    x, y = xy[0], xy[1]
    patches += broken_line(xy, w, h, spacing)
    patches += line((x, y - spacing - h), w, h)
    patches += line((x, y - 2 * (spacing + h)), w, h)
    return patches

def li(xy = (0, 1.), w = 1.1, h = .1, spacing = 0.1):
    """
    Li(Fire)
    """
    patches = []
    x, y = xy[0], xy[1]
    patches += line(xy, w, h)
    patches += broken_line((x, y - spacing - h), w, h, spacing)
    patches += line((x, y - 2 * (spacing + h)), w, h)
    return patches

def zhen(xy = (0, 1.), w = 1.1, h = .1, spacing = 0.1):
    """
    Zhen(Thunder)
    """
    patches = []
    x, y = xy[0], xy[1]
    patches += broken_line(xy, w, h, spacing)
    patches += broken_line((x, y - spacing - h), w, h, spacing)
    patches += line((x, y - 2 * (spacing + h)), w, h)
    return patches

def xun(xy = (0, 1.), w = 1.1, h = .1, spacing = 0.1):
    """
    Xun(Wind)
    """
    patches = []
    x, y = xy[0], xy[1]
    patches += line(xy, w, h)
    patches += line((x, y - spacing - h), w, h)
    patches += broken_line((x, y - 2 * (spacing + h)), w, h, spacing)
    return patches

def kan(xy = (0, 1), w = 1.1, h = .1, spacing = 0.1):
    """
    Kan(Water)
    """
    patches = []
    x, y = xy[0], xy[1]
    patches += broken_line(xy, w, h, spacing)
    patches += line((x, y - spacing - h), w, h)
    patches += broken_line((x, y - 2 * (spacing + h)), w, h, spacing)
    return patches

def gen(xy = (0, 1), w = 1.1, h = .1, spacing = 0.1):
    """
    Gen(Mountain)
    """
    patches = []
    x, y = xy[0], xy[1]
    patches += line(xy, w, h)
    patches += broken_line((x, y - spacing - h), w, h, spacing)
    patches += broken_line((x, y - 2 * (spacing + h)), w, h, spacing)
    return patches

def kun(xy = (0, 1), w = 1.1, h = .1, spacing = 0.1):
    """
    Kun(Earth)
    """
    patches = []
    x, y = xy[0], xy[1]
    patches += broken_line(xy, w, h, spacing)
    patches += broken_line((x, y - spacing - h), w, h, spacing)
    patches += broken_line((x, y - 2 * (spacing + h)), w, h, spacing)
    return patches

def hexagram(ax, top, bottom, xy = (0, 1.), w = 1.1, h = .1, spacing = .1):
    x, y = xy[0], xy[1]
    patches = PatchCollection(top(xy = xy, w = w, h = h, spacing = spacing))
    patches.set_color('black')
    ax.add_collection(patches)
    bottom_y =  y - (h + spacing) * 3
    patches = PatchCollection(bottom(xy = (x, bottom_y), w = w, h = h , spacing = spacing))
    patches.set_color('black')
    ax.add_collection(patches)


# 乾一、兑二、离三、震四、巽五、坎六、艮七、坤八
_hexagram = { '000': kun, '001': gen, '010': kan, '011': xun, '100': zhen, '101': li, '110': dui, '111': qian }

def gen():
    # 天道左旋，地道右旋
    for heaven_k, heaven_v in _hexagram.items():
        for earth_k, earth_v in _hexagram.items():
            _, ax = plt.subplots()
            hexagram(ax, heaven_v, earth_v)
            plt.axis('equal')
            plt.axis('off')
            plt.tight_layout()
            plt.savefig('docs/hexagram/{}.png'.format(heaven_k + earth_k))
            plt.close()
