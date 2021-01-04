"""
易经六十四卦
"""

from enum import Enum
from pickles.chings import hexagrams


_TRIGRAMS = ['坤', '艮', '坎', '巽', '震', '离', '兑', '乾']


_HEXAGRAM = [
    0X3F, 0X00, 0X22, 0X11, 0X3A, 0X17, 0X10, 0X02, 
    0X3B, 0X37, 0X38, 0X07, 0X2F, 0X3D, 0X08, 0X04, 
    0X26, 0X19, 0X30, 0X03, 0X25, 0X29, 0X01, 0X20, 
    0X27, 0X39, 0X21, 0X1E, 0X12, 0X2D, 0X0E, 0X1C, 
    0X0F, 0X3C, 0X05, 0X28, 0X2B, 0X35, 0X0A, 0X14, 
    0X31, 0X23, 0X3E, 0X1F, 0X06, 0X18, 0X16, 0X1A, 
    0X2E, 0X1D, 0X24, 0X09, 0X0B, 0X34, 0X2C, 0X0D, 
    0X1B, 0X36, 0X13, 0X32, 0X33, 0X0C, 0X2A, 0X15
]


class Hexagram:

    """
    卦，分上下卦，共六爻

    Attributes:
        changes (int): 本卦 转二进制（1-阳、0-阴）六爻，初爻 -> 上爻 
        changed (int): 变卦
        change_lines (list): 变爻列表
    """

    def __init__(self, lower, upper):
        """Inits Hexagram
        
        Args:
            lower (Trigram): 下卦
            upper (Trigram): 上卦
        """
        self._changes = (lower.value << 3) + upper.value
        self._changed = None
        self._change_lines = []

    @property
    def changes(self):
        return _HEXAGRAM.index(self._changes)

    @property
    def changed(self):
        return _HEXAGRAM.index(self._changed)

    def is_changed(self):
        return self._changed is not None

    def change(self, change_lines):
        if not change_lines or self.is_changed():
            return
        self._changed = self._changes
        for line in change_lines:
            self._changed ^= (1 << ((6 - line) % 6))
        self._change_lines = change_lines
    
    @property
    def lower_trigram(self):
        return _TRIGRAMS[self._changes >> 3]
    
    @property
    def upper_trigram(self):
        return _TRIGRAMS[self._changes & 0x7]

    @property
    def change_lines(self):
        return self._change_lines

    def details(self, i = 0):
        idx = self._changes if i == 0 else self._changed
        return hexagrams[_HEXAGRAM.index(idx)]

    def __str__(self):
        # # 九-阳 六-阴 初爻 -> 上爻
        sign = []
        nums = ['初', '二', '三', '四', '五', '上']
        for i, num in enumerate(nums):
            n = (self._changes >> (5 - i)) & 1
            state = '六' if n == 0 else '九'
            sign.append(num + state if i == 0 or i == 5 else state + num)
        return str(sign)


class Trigram(bytes, Enum):

    """
    八卦：乾一、兑二、离三、震四、巽五、坎六、艮七、坤八
    """

    def __new__(cls, idx = 7, name = '乾'):
        obj = bytes.__new__(cls, [idx])
        obj._value_ = idx
        obj.trigram = name
        return obj

    @staticmethod
    def trigram(name):
        return Trigram(_TRIGRAMS.index(name))

    @property
    def name(self):
        return self.trigram

    def __add__(self, other):
        return Hexagram(self, other)
    
    Heaven = (7, '乾')
    Lake = (6, '兑')
    Fire = (5, '离')
    Thunder = (4, '震')
    Wind = (3, '巽')
    Water = (2, '坎')
    Mountain = (1, '艮')
    Earth = (0, '坤')