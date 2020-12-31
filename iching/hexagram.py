"""
易经六十四卦
"""

from trigram import TRIGRAMS


# Trigram
class Hexagram:

    """
    卦，分上下卦，共六爻

    Attributes:
        id (int): 卦号 
        name (str): 卦名
        lower_trigram (Trigram): 下卦
        upper_trigram (Trigram): 上卦
        changes (list): 六爻，初爻 -> 上爻
    """

    def __init__(self, id, name, lower_trigram, upper_trigram, changes):
        """Inits Hexagram"""
        self.id = id
        self.name = name
        self.lower_trigram = lower_trigram
        self.upper_trigram = upper_trigram

    def __str__(self):
        return '卦{} {}上{}下'.format(self.id, self.upper_trigram.name, self.lower_trigram.name)
