"""干支纪法
Chronography - chronology

甲子周期：
    '甲子', '乙丑', '丙寅', '丁卯', '戊辰', '己巳', '庚午', '辛未', '壬申', '癸酉',
    '甲戌', '乙亥', '丙子', '丁丑', '戊寅', '己卯', '庚辰', '辛巳', '壬午', '癸未',
    '甲申', '乙酉', '丙戌', '丁亥', '戊子', '己丑', '庚寅', '辛卯', '壬辰', '癸巳',
    '甲午', '乙未', '丙申', '丁酉', '戊戌', '己亥', '庚子', '辛丑', '壬寅', '癸卯',
    '甲辰', '乙巳', '丙午', '丁未', '戊申', '己酉', '庚戌', '辛亥', '壬子', '癸丑', 
    '甲寅', '乙卯', '丙辰', '丁巳', '戊午', '己未', '庚申', '辛酉', '壬戌', '癸亥'

干支计时：
    子时（夜11至1点）   丑时（后半夜1至3点）寅时（后半夜3至5点）卯时（早晨5至7点）
    辰时（早晨7至9点）  巳时（上午9至11点） 午时（上午11至1点） 未时（下午1至3点）  
    申时（下午3至5点）  酉时（下午5至7点）  戌时（晚7至9点）    亥时（晚9至11点）
"""

import datetime


# 甲子年 甲子日
CE = datetime.date(1984, 3, 31)
# 天干
HEAVENLY = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
# 地支
EARTHLY = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']

# 甲子周期
TERM = [
    0x03EA, 0x045A, 0x04CA, 0x053A, 0x05A0, 0x0610, 0x0680, 0x06F0, 0x0760, 0x07C6, 
    0x2776, 0x2B6A, 0x04B6, 0x0526, 0x058C, 0x05FC, 0x066C, 0x06DC, 0x074C, 0x07B2, 
    0x043A, 0x04AA, 0x2F4A, 0x333E, 0x0578, 0x05E8, 0x0658, 0x06C8, 0x0738, 0x079E, 
    0x0426, 0x0496, 0x0506, 0x0576, 0x3714, 0x3B08, 0x0644, 0x06B4, 0x0724, 0x078A, 
    0x0412, 0x0482, 0x04F2, 0x0562, 0x05C8, 0x0638, 0x3EE8, 0x42DC, 0x0710, 0x0776, 
    0x03FE, 0x046E, 0x04DE, 0x054E, 0x05B4, 0x0624, 0x0694, 0x0704, 0x46BC, 0x4AA6
]

term = lambda delta: '{:03d}'.format(TERM[delta % 60])

def extract(i):
    shex = '{:03d}'.format(TERM[i])
    return HEAVENLY[int(shex[1])] + EARTHLY[int(shex[2:-1])], int(shex[-1])


def year(y):
    """元年转干支"""
    tm = term(abs(y - CE.year))
    return HEAVENLY[tm % 10] + EARTHLY[tm % 12]

def birthdates(y, m, d, h):
    """获取生辰八字
    
    Args: 
        birthdate (str): 年月日时（%Y%m%d%H: 2001102312）

    Returns: 年月日时四柱干支
    """
    date = datetime.date(y, m, d)
    # 年柱
    year_delta = abs(y - CE.year)
    year, m_h = extract(year_delta % 60)
    # 月柱
    m_h = (m_h + m - 2) % 10
    m_e = m % 12
    month = HEAVENLY[m_h] + EARTHLY[m_e]
    # 日柱
    day_delta = (date - CE).days
    day, _ = extract(day_delta % 60)
    # TODO 年退位、时柱
    return [year, month, day, '']

def chronologies():
    """返回甲子纪年表"""
    HE = []
    i = j = 0
    while True:
        he = HEAVENLY[i] + EARTHLY[j]
        if he in HE:
            break
        HE.append(he)
        i = 0 if i == 9 else i + 1
        j = 0 if j == 11 else j + 1
    return HE
