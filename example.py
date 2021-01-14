import argparse
from miching.horoscope import Prophet
from miching.version import __version__


def usage():
    parser = argparse.ArgumentParser(description = "Any vital question you may have, ask it here.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-q', dest= 'question', help = "the question you are going to ask for")
    group.add_argument('-t', dest= 'topic', help = "the topic about your question")
    parser.add_argument('-s', dest = 'seed', type=int, help = "the random seed (not recommended)")
    parser.add_argument('-v', dest = 'visual', action="store_true", help = "visualizing the prophesy process")
    parser.add_argument('-o', dest = 'output', help = "write to file instead of stdout")
    parser.add_argument('-V', '--version', action = 'version', version = __version__, help = "show this version message and exit")
    args = parser.parse_args()
    # 易经预测
    prophet = Prophet(event = args.topic, seed = args.seed)
    prophet.prophesy()
    prophet.explain()
    if args.visual: prophet.visualize()


if __name__ == '__main__':
    usage()
    
