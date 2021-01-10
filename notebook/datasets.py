import json
import jieba
import parsel
import requests
from itertools import islice

# http://www.360doc.com/content/18/0728/06/42860393_773759238.shtml

url = 'http://www.360doc.com/content/18/0728/06/42860393_773759238.shtml'
resp = requests.get(url)
html = parsel.Selector(resp.text)



# 初难知，二多誉，三多凶，四多惧，五多功，上易知
severities = {
    '1.1': '学业烦恼、对未来规划的迷茫', '1.2': '事业和工作烦恼', '1.3': '家庭问题和矛盾', '1.4': '物质滥用',
    '1.5': '悲恸', '1.6': '失眠', '1.7': '压力', '1.8': '人际关系', '1.9': '情感关系问题', '1.10': '离婚',
    '1.11': '分手', '1.12': '自我探索', '1.13': '低自尊', '1.14': '青春期问题', '1.15': '强迫症', 
    '1.16': '其它', '1.17': '男同性恋、女同性恋、双性恋与跨性别', '1.18': '性问题', '1.19': '亲子关系'
}

# with open('EFA_Dataset_v20200314_latest.txt', 'r', encoding='utf8') as rf:
#     vocab = []
#     while True:
#         lines = list(islice(rf, 64))
#         if not lines: break
#         for line in lines:
#             js = json.loads(line)
#             title = js['title']
#             label = severities[js['label']['s1']]
#             print(label, title)


"""
学业：
事业：
家庭：
情感：
健康：
决策：

ID	中文	英文	备注
1.1	学业烦恼、对未来规划的迷茫	Academic Concerns	学业烦恼包括学习障碍、学习吃力、学习成绩差、注意力不集中和对学习科目无兴趣等。
1.2	事业和工作烦恼	Career and Workplace Issues	在工作中的，人际冲突问题、沟通问题、谣言、职场骚扰、歧视、动力不足和工作满意度低和职场表现差等问题。
1.3	家庭问题和矛盾	Family Issues and Conflict	家庭问题和矛盾包括家庭暴力、金钱遗产争执、家庭不和睦、婆媳问题、子女们对年长父母看护问题、继父母继子女冲突问题和离异父母对于儿女的养护问题。
1.4	物质滥用	Substance Abuse and Addiction	成人如酗酒、吸烟、药物滥用、吸毒、赌博和任何影响生活品质的上瘾行为。
1.5	悲恸	Grief	由于痛失亲人或朋友而引起的极大悲伤。
1.6	失眠	Insomnia	无法入睡或难以保持入睡状态而影响第二天表现的睡眠障碍。
1.7	压力	Stress	压力是一种情绪上或身体上的紧张感。它可能来自任何使您感到沮丧，愤怒或紧张的事件或想法。
1.8	人际关系	Interpersonal Relationship	不属于职场、学校以及家庭的人际关系紧张与矛盾。
1.9	情感关系问题	Relationship Issues	早恋、暗恋、异地恋、出轨、吵架、复合、LGBT 群体
1.10	离婚	Divorce	离婚后情感以及孩子的问题
1.11	分手	Break Up	分手后的痛苦
1.12	自我探索	Self-Awareness	如星座、性格、兴趣等
1.13	低自尊	Low self-esteem	低自尊心的表现 自尊是一个人对自己的价值的主观评价。自尊包括对自己以及情绪状态的信念，例如胜利，绝望，骄傲和羞耻。
1.14	青春期问题	Adolescent Problem	青春期少年在身心成长上所面临的问题，如叛逆、伤害他人、怀孕、药物滥用和青少年犯罪。
1.15	强迫症	OCD	强迫症的人会陷入一种无意义、且令人沮丧的重复的想法与行为当中，但是一直想却无法摆脱它。
1.16	其它	Others	其他烦恼，虽然对生活学习没有造成毁灭性的阻碍，但是却依然会引起心里不适。
1.17	男同性恋、女同性恋、双性恋与跨性别	LGBT	男同性恋、女同性恋、双性恋与跨性别
1.18	性问题	Sex	对于青少年，是性教育不足引起各种社会问题；对于成年人，性焦虑与性上瘾可以演变成生理疾病。
1.19	亲子关系	Parent-child relationship	亲子关系，从婴幼儿时期就开始影响着孩子各方面的发展，比如性格、毅力、人际交往等等。

"""