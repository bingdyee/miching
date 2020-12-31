"""
八卦：乾一、兑二、离三、震四、巽五、坎六、艮七、坤八
"""


TRIGRAMS = ['坤', '艮', '坎', '巽', '震', '离', '兑', '乾']

trigram = lambda t: '{:03b}'.format(t if isinstance(t, int) else TRIGRAMS.index(t))


class Trigram:

    def __init__(self, name):
        self.name = name
        self.bin = trigram(name)
